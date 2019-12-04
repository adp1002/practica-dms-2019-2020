from logica.logica_client import LogicaCliente
from presentacion.en_terminal import EnTerminal


'''Comienzo del script'''


'''
Registro y/o Login del usuario
'''
#Inicializamos el token del jugador a None
token = None

while(token is None):
    username,password = EnTerminal.pedir_usuario()
    #Creamos el usuario
    LogicaCliente.registrar_usuario(username,password)
    print('\nLogueando...\n')
    token = LogicaCliente.loguear_usuario(username,password)
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
    lista_servidores = LogicaCliente.obtener_servidores(token)
    EnTerminal.listar_servidores(lista_servidores)
    no_servidor_seleccionado = EnTerminal.escoger_servidor(lista_servidores)

    if(lista_servidores is not None):
        #Registramos al usuario en servidor. Si no puede, volvemos a mostrar la lista de servidores.
        servidor_de_juego = LogicaCliente.registrarse_en_servidor(token,lista_servidores[no_servidor_seleccionado])
    else:
        if(input('¿Repetir la busqueda? (S/N): ') in ['N','n']):
            exit()


'''
Juego
'''
#Comenzamos el bucle de pedir tablero y jugar
while(not servidor_de_juego.esta_acabado()):

        #Dibujo del tablero de esta iteraccion
        tablero_actual = servidor_de_juego.get_tablero()
        if(tablero_actual):
            EnTerminal.dibujar_tablero(tablero_actual)
        else:
            print("\nError al obtener el tablero. Abortando cliente...\n")
            exit()
        
        #Comprobamos si es nuestro turno y jugamos
        nuestro_turno = servidor_de_juego.get_turno(token)
        #Mostramos por pantalla si es nuestro trno o no
        EnTerminal.es_turno(nuestro_turno)
        #Si es nuestro turno, pedimos jugada
        if(nuestro_turno):
            jugada_realizada = False
            while(not jugada_realizada):
                x,y = EnTerminal.pedir_jugada()
                jugada_realizada = LogicaCliente.realizar_jugada(token,servidor_de_juego,x,y)
                if(not jugada_realizada):
                        print('Jugada incorrecta. Coordenadas erroneas.')
            
            #Volvemos a dibujar el tablero despues de jugar
            EnTerminal.dibujar_tablero(servidor_de_juego.get_tablero())
            
        #Pauser bucle hasta nuevo input.
        input('Pulsa una tecla para actualizar.\n')

'''
Fin de partida. Mostrando resultados.
'''
EnTerminal.mostrar_resultados(token,servidor_de_juego)
LogicaCliente.finalizar_partida(token,servidor_de_juego)

'''
Mostrando score global
'''
score = LogicaCliente.get_score()
EnTerminal.mostrar_score(score)

