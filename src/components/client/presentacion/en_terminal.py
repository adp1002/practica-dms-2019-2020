"""
Clase EnTerminal es un clase con metodos estaticos.
Representa los datos por un terminal y devuelve los inputs del usuario.
"""

class EnTerminal:
    """ Obtiene los datos para registrar y loguear al usuario en el servidor
    ---
    Returns:
        El username y password introducidos por el usuario
    """
    @staticmethod
    def pedir_usuario():
        username = input('Introduce el nombre del usuario:\n')
        password = input('Introduce la contraseña del usuario:\n')
        return username,password

    """ Muestra la lista de servidores activos
    ---
    Parameters:
        - servidores_activos: La lista de servidores activos a representar
    """
    @staticmethod
    def listar_servidores(servidores_activos):
        if(servidores_activos is None or not servidores_activos):
                print('¡No hay servidores de juego activos!')

        #Listamos los servidores
        else:
            for idx,servidor in enumerate(servidores_activos):
                print(str(idx) + ". " + servidor['name'] + " (" + servidor['host'] + ":" + servidor['port'] + ")")

    """ Permite al usuario elegir un servidor entre los servidores activos
    ---
    Parameters:
        - servidores_activos: La lista de servidores activos
    Returns:
        El numero del servidor seleccionado
    """
    @staticmethod
    def escoger_servidor(servidores_activos):
        servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
        while (int(servidor_elegido) > len(servidores_activos)):
            print("¡Servidor fuera de rango!")
            servidor_elegido = input("\nEscribe el numero del servidor de juego que quieras: ")
        return int(servidor_elegido)

    """ Dibuja una matriz 
    ---
    Parameters:
        - tablero: Matriz a dibujar
    """
    @staticmethod
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

    """ Muestra por pantalla un mensaje indicando si es tu turno
    ---
    Parameters:
        - es_tu_turno: Booleano que representa si es tu turno o no
    """
    @staticmethod
    def es_turno(es_tu_turno):
        if(es_tu_turno):
            print('\n¡Tu turno!\n')
        else:
            print('\nAun no es tu turno.\n')


    """ Pide las cooredenadas x e y por pantalla
    ---
    Returns:
        Las coordenadas x e y introducidas por pantalla
    """
    @staticmethod
    def pedir_jugada():
            print('\n¡Tu turno!\n')
            x = input('Introduce la cordenada x: ')
            y = input('Introduce la cordenada y: ')
            return x,y

    """ Muestra el resultado de una partida
    ---
    Parameters:
        - token: El token del usuario que realiza la petición
        - servidor_seleccionado: el servidor seleccionado en el que va a jugando el usuario
    """
    @staticmethod
    def mostrar_resultados(token,servidor_de_juego):
        print('\n\n¡Partida finalizada! Mostrando el tablero final:\n')
        EnTerminal.dibujar_tablero(servidor_de_juego.get_tablero())
        print(servidor_de_juego.get_resultado(token))

    """ Muestra el score
    ---
    Parameters:
        - score: La lista de scores que se quiere representar
    """
    @staticmethod
    def mostrar_score(scores):
        print('\nScores:\n')
        if(scores):
            for idx,score in enumerate(scores, 1):
                print(idx,'- ', score['username'], ' ', score['score'],
                    ' (', score['games_won'], '/', score['games_lost'], ')')