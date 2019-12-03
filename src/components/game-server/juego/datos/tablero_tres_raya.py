from juego.datos.tablero_abstracto import TableroAbstracto

class TableroTresRaya(TableroAbstracto):
    """ Clase que representa un tablero del tres en raya.
    ---
    La clase almacena las piezas del tres en raya.
    """

    FILAS = 3
    COLUMNAS = 3

    def __init__(self):
        """Constructor.
        ---
        Inicializa el un tablero vacío.
        """
        super().__init__(TableroTresRaya.FILAS, TableroTresRaya.COLUMNAS)
