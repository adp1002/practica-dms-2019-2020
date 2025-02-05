from juego.fabrica_abstracta_juegos import FabricaJuegoMesa

class Partida:
    """ Partida de un juego entre dos jugadores.
    ---
    La clase almacena el estado de la partida.
    """

    def __init__(self, fabrica_juego):
        """ Constructor.
        ---
            Parámetros:
                - fabrica_juego: FabricaJuegoMesa
                - jugador1: Jugador 1.
                - jugador2: Jugador 2.
        """
        self.__jugador1 = None
        self.__jugador2 = None
        self.__fabrica = fabrica_juego
        self.__tablero = fabrica_juego.crear_tablero()
        self.__arbitro = fabrica_juego.crear_arbitro(self.__tablero)
        self.__turno = 0
        self.__ganador = None
        
    def registrar_jugador(self, jugador):
        """ Método que añade un jugador a la partida.
        ---
            Parámetros:
                - jugador: Jugador a registrar.
            Returns:
                True si hay espacio en la partida, sino False.
        """
        if self.__jugador1 is None:
            self.__jugador1 = jugador
            self.__jugador1.establecer_tipo('X')
        elif self.__jugador2 is None:
            self.__jugador2 = jugador
            self.__jugador2.establecer_tipo('O')
        else:
            return False
        return True

    def jugar(self, x, y):
        """ Método que realiza un movimiento.
        ---
        Parámetros:
            - x: Fila del tablero.
            - y: Columna del tablero.
        """
        if self.__arbitro.es_valido(x, y):
            self.__tablero.colocar(x, y,
                self.__fabrica.crear_pieza(self.obtener_turno().obtener_tipo()))
            self.__turno += 1
        else:
            raise Exception('Partida llena')

    def obtener_ganador(self):
        """ Método que devuelve el ganador de la partida.
        ---
        Returns:
            El Jugador ganador, si no hay ganador None
        """
        if self.__arbitro.hay_ganador():
            return self.__jugador1 if self.__turno % 2 != 0 else self.__jugador2
        return None

    def obtener_perdedor(self):
        """ Método que devuelve el perdedor de la partida.
        ---
        Returns:
            El Jugador perdedor, si no hay perdedor None
        """
        if self.__arbitro.hay_ganador():
            return self.__jugador1 if self.__turno % 2 == 0 else self.__jugador2
        return None

    def esta_acabado(self):
        """ Método que decide si la partida ha terminado.
        ---
        Returns:
            True si la partida esta terminada, sino False
        """
        return self.__arbitro.esta_acabado()

    def obtener_turno(self):
        """ Método que obtiene el jugador con el turno.
        ---
        Returns:
            Jugador con el turno.
        """
        return self.__jugador1 if self.__turno % 2 == 0 else self.__jugador2

    def obtener_tablero(self):
        """ Método que devuelve el tablero de la partida.
        ---
        Returns:
            Tablero de la partida.
        """
        return self.__tablero
