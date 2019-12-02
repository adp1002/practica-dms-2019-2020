from juego.modelo.tablero_abstracto import TableroAbstracto

class TableroConectaCuatro(TableroAbstracto):
    """ Clase que representa un tablero del tres en raya.
    ---
    La clase almacena las piezas del tres en raya.
    """

    MAX_PIEZAS = 42

    def __init__(self, ancho, alto):
        """Constructor.
        ---
        Inicializa el un tablero vacío.
        """
        super().__init__(ancho, alto)

    def esta_lleno(self):
        """ Método que comprueba si el tablero esta lleno.
        ---
        Returns:
            True si el tablero esta lleno, sino False.
        """
        return self.__piezas == TableroTresRaya.MAX_PIEZAS
