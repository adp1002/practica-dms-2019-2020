from conexiones.auth_client import AuthClient
from conexiones.hub_client import HubClient
from conexiones.game_client import GameClient

""" Saca por pantalla un listado de servidores activos y pide al usuario que escoga uno.
---
Returns:
    Un array con la información del servidor escogido
"""
def seleccion_de_servidor():
    print('Listando servidores activos...\n')
    peticion_repetir = '0'
    #Bucle para pedir servidores
    while(peticion_repetir not in ['N','n']):
        servidores_activos = HubClient.instance().get_servers(token)

        #Si no hay servidores activos, se puede repetir la busqueda o salir
        if(servidores_activos is None or not servidores_activos):
            print('¡No hay servidores de juego activos!')
            while(peticion_repetir not in ['S','s','exit']):
                peticion_repetir = input('¿Quieres repetir la busqueda? (S/exit): ')
                if(peticion_repetir == 'exit'):
                    exit()

        #Listamos los servidores
        else:
            peticion_repetir = 'N'
            for idx,servidor in enumerate(servidores_activos):
                print(str(idx) + ". " + servidor['name'] + " (" + servidor['host'] + ":" + servidor['port'] + ")")

            #Escogemos un servidor
            servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
            while (int(servidor_elegido) > len(servidores_activos)):
                print("¡Servidor fuera de rango!")
                servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
    return servidores_activos[int(servidor_elegido)]


""" Registra al usuario actual en el servidor pasado por parametro
---
Parameters:
    - servidor_seleccionado: Array con la informacion del servidor seleccionado para registrar al usuario
Returns:
    El servidor de juego o None si ha surgido un error.
"""
def registrarse_en_servidor(servidor_seleccionado):
    servidor_de_juego = GameClient(servidor_seleccionado['host'],servidor_seleccionado['port'])
    if((servidor_de_juego is None) or (not servidor_de_juego.registrar_usuario_en_servidor(token))):
        print('\nHa ocurrido un error al intentar entrar al servidor. Intenta probar en un nuevo servidor.\n')
        return None
    else:
        return servidor_de_juego

""" Dibuja una matriz 
---
Parameters:
    - tablero: Matriz a dibujar
"""
def dibujar_tablero(tablero):
    for idx,fila in enumerate(tablero):
        #Print de numero en columna
        if (idx == 0):
            print('      ', end ='')
            for i in range(len(fila)):
                print(i,'  ', end ='')
            print('\n')
        print(idx,'. | ', end ='')
        for casilla in fila:
            if (casilla is None):
                casilla = ' '
            print(casilla,'| ',end = '')
        print('\n')








'''Comienzo del script'''
'''
Registro y/o Login del usuario
'''
#Inicializamos el token del jugador a None
token = None

while(token is None):
    username = input('Introduce el nombre del usuario:\n')
    password = input('Introduce la contraseña del usuario:\n')
    #Creamos el usuario
    AuthClient.instance().registrar(username,password)
    print('\nLogueando...\n')
    token = AuthClient.instance().login(username,password)
    if(token is None):
        if(input('Usuario incorrecto. ¿Volver a introducir usuario? (S/N): ') in ['N','n']):
            exit()
    else:
        print('Usuario autentificado correctamente.')


'''
Listado y seleccion de los servidores de juego
'''
#Inicializamos el servidor de juego a None
servidor_de_juego = None

while(servidor_de_juego is None):
    #Seleccionamos el servidor con la funcion seleccion_de_servidor
    servidor_seleccionado = seleccion_de_servidor()
    #Registramos al usuario en servidor. Si no puede, volvemos a mostrar la lista de servidores.
    servidor_de_juego = registrarse_en_servidor(servidor_seleccionado)


'''
Juego en el cliente
'''
#Comenzamos el bucle de pedir tablero y jugar
while(not servidor_de_juego.esta_acabado()):

    #Dibujo del tablero de esta iteraccion
    tablero_actual = servidor_de_juego.get_tablero()
    if(tablero_actual):
        dibujar_tablero(tablero_actual)
    else:
        print("\nError al obtener el tablero. Abortando cliente...\n")
        exit()
    
    #Comprobamos si es nuestro turno y jugamos
    nuestro_turno = servidor_de_juego.get_turno(token)
    if(nuestro_turno):
        print('\n¡Tu turno!\n')
        #Bucle para asegurarse de que la jugada es aceptada por servidor
        es_jugada_valida = False
        while(not es_jugada_valida):
            x = input('Introduce la cordenada x: ')
            y = input('Introduce la cordenada y: ')
            es_jugada_valida = servidor_de_juego.jugar(token,x,y)
            if(not es_jugada_valida):
                print('Jugada incorrecta. Coordenadas erroneas.')
        #Volvemos a dibujar el tablero despues de jugar
        tablero_actual = servidor_de_juego.get_tablero()
        dibujar_tablero(tablero_actual)

    else:
        print('\nAun no es tu turno.\n')
    
    #Pauser bucle hasta nuevo input.
    input('Pulsa una tecla para actualizar.\n')

'''
Fin de partida. Mostrando resultados.
'''
print('\n\n¡Partida finalizada! Mostrando el tablero final:\n')
tablero_actual = servidor_de_juego.get_tablero()
dibujar_tablero(tablero_actual)
print(servidor_de_juego.get_resultado(token))
servidor_de_juego.finalizar_partida(token)

'''
Mostrando score global
'''
print('\nScores:\n')
scores = AuthClient.instance().get_score()
if(scores):
    for idx,score in enumerate(scores):
        print(idx,'- ', score['username'], ' ', score['score'],
            ' (', score['games_won'], '/', score['games_lost'], ')')

