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
    peticion_repetir = 'S'
    #Bucle para pedir servidores
    while(peticion_repetir not in ['N','n']):
        servidores_activos = HubClient.instance().get_servers(token)
        if(servidores_activos is None or not servidores_activos):
            #Si no hay servidores activos, se repite la busqueda o se sale
            print('¡No hay servidores de juego activos!')
            peticion_repetir = input('¿Quieres repetir la busqueda? (S/exit): ')
            if(peticion_repetir in ['N','n']):
                print('Para jugar necesitar un servidor.')
                peticion_repetir = 'S'
            elif(peticion_repetir == 'exit'):
                exit()
        else:
            for idx,servidor in enumerate(servidores_activos):
                print(str(idx) + ". " + servidor['name'] + " (" + servidor['host'] + ":" + servidor['port'] + ")")

            #Ofrecemos la opcion de repetir la busqueda antes de seleccionar un servidor
            peticion_repetir = input('¿Quieres repetir la busqueda? (S/N/exit): ')
            if(peticion_repetir in ['N','n']):
                #Si no quiere repeter la busqueda, escogemos un servidor
                servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
                while (int(servidor_elegido) > len(servidores_activos)):
                    print("¡Servidor fuera de rango!")
                    servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
            elif(peticion_repetir == 'exit'):
                exit()
    return servidores_activos[int(servidor_elegido)]

""" Registra al usuario actual en el servidor pasado por parametro
---
Parameters:
    - servidor_seleccionado: Array con la informacion del servidor seleccionado para registrar al usuario
Returns:
    True si se ha registrado correctamente, si no, False
"""
def registrarse_en_servidor(servidor_seleccionado):
    servidor_de_juego = GameClient(servidor_seleccionado['host'],servidor_seleccionado['port'])
    if((servidor_de_juego is None) or (not servidor_de_juego.registrar_usuario_en_servidor(token))):
        print('\nHa ocurrido un error al intentar entrar al servidor. Intenta probar en un nuevo servidor.\n')
        return False
    else:
        return True

""" Dibuja una matriz 
---
Parameters:
    - tablero: Matriz a dibujar
"""
def dibujar_tablero(tablero):
    for fila in tablero_inicial:
        print('| ', end ='')
        for casilla in fila:
            print(casilla,end = '')
            print(' |',end = '')
    print('')



'''Comienzo del script'''
#Obtenemos los datos del usuario
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



#Seleccionamos el servidor con la funcion seleccion_de_servidor
servidor_seleccionado = seleccion_de_servidor()

#Registramos al usuario en servidor. Si no puede, volvemos a mostrar la lista de servidores.
while(not registrarse_en_servidor(servidor_seleccionado)):
    servidor_seleccionado = seleccion_de_servidor()

#Comenzamos el bucle de pedir tablero y jugar
while(not servidor_de_juego.esta_acabado()):
    tablero_actual = servidor_de_juego.get_tablero()
    if(tablero_actual is None):
        print("\nError al obtener el tablero. Abortando cliente...\n")
        exit()
    else:
        dibujar_tablero(tablero_actual)
    
    #Comprobamos si es nuestro turno.
    nuestro_turno = servidor_de_juego.get_turno(token)
    if(nuestro_turno):
        print('\n¡Tu turno!\n')
        es_jugada_valida = False
        while(not es_jugada_valida):
            coor_x = input('Introduce la cordenada x: ')
            coor_y = input('Introduce la cordenada y: ')
            es_jugada_valida = servidor_de_juego.jugar(token,x,y)
            if(not es_jugada_valida):
                print('Jugada incorrecta. Coordenadas erroneas.')
        #Volvemos a dibujar el tablero despues de jugar
        tablero_actual = servidor_de_juego.get_tablero()
        dibujar_tablero(tablero_actual)
    else:
        print('\nAun no es tu turno.\n')
        
        input('Pulsa una tecla para actualizar.')

print('¡Partida finalizada! Mostrando el tablero final:')
tablero_actual = servidor_de_juego.get_tablero()
dibujar_tablero(tablero_actual)
print(servidor_de_juego.get_resultado())