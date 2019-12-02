from juego.datos.tablero_abstracto import TableroAbstracto

class TableroTresRaya(TableroAbstracto):
    """ Clase que representa un tablero del tres en raya.
    ---
    La clase almacena las piezas del tres en raya.
    """

    MAX_PIEZAS = 9

    def __init__(self):
        """Constructor.
        ---
        Inicializa el un tablero vacío.
        """
        self.__tablero = [[None, None, None], [None, None, None], [None, None, None]]
        self.__piezas = 0

    def colocar(self, x, y, pieza):
        """ Método que coloca un pieza en las coordenadas.
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
        return self.__piezas == TableroTresRaya.MAX_PIEZAS

    def obtener_array(self):
        """ Método que devuelve el tablero en forma de matriz.
        ---
        Returns:
            Una matriz con el contenido del tablero.
        """
        return self.__tablero

    def __str__(self):
        return str(self.__tablero)
