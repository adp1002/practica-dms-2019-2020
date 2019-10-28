from juego.modelo.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

    def __init__(self, tablero, jugador1, jugador2):
        """Constructor.
        ---
            Parámetros:
                - tablero: tablero de la partida.
                - jugador1: Jugador 1.
                - jugador2: Jugador 2.
        """
        self.__tablero = tablero
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__turno = 0

    def jugar(self, x, y):
        if self.es_valido(x,y):
            self.__tablero.colocar(x,y)

    def es_valido(self, x, y):
        return x >= 0 or y >= 0 or x <= 2 or y <= 2 \
            or self.__tablero.obtener_pieza(x,y) is None          


    def obtener_ganador(self):
        pass

    def obtener_turno(self):
        if self.__turno:
            return self.__jugador1
        else:
            return self.__jugador2
