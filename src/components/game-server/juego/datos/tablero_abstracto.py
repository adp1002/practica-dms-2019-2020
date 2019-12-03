from abc import ABC, abstractmethod

class TableroAbstracto(ABC):
    """ Clase abstracta que representa un tablero.
    ---
    La clase proporciona la estructura de una tablero.
    """

    def __init__(self, ancho, alto):
        self.__tablero = [[None]*ancho  for _ in range(alto)]
        self.__piezas = 0
        self.__max_piezas = ancho * alto

    def colocar(self, x, y, pieza):
        """ Método que coloca una pieza en las coordenadas.
        ---
        Parámetros:
            - x: Fila del tablero.
            - y: Columna del tablero.
            - pieza: Pieza a colocar.
        """
        self.__tablero[x][y] = pieza
        self.__piezas += 1

    def obtener_pieza(self, x, y):
        """ Método que devuelva la pieza de las coordenadas.
        ---
        Parametros:
            - x: Fila del tablero.
            - y: Columna del tablero.
        Returns:
            Pieza del tablero.
        """
        return self.__tablero[x][y]

    def esta_lleno(self):
        """ Método que comprueba si el tablero esta lleno.
        ---
        Returns:
            True si el tablero esta lleno, sino False.
        """
        return self.__piezas == self.__max_piezas

    def obtener_array(self):
        """ Método que devuelve el tablero en forma de matriz.
        ---
        Returns:
            Una matriz con el contenido del tablero.
        """
        return self.__tablero

    def __str__(self):
        return str(self.__tablero)
