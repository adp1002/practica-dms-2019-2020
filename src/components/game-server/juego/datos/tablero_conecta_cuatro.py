from juego.datos.tablero_abstracto import TableroAbstracto

class TableroConectaCuatro(TableroAbstracto):
    """ Clase que representa un tablero del conecta 4.
    ---
    La clase almacena las piezas del conecta 4.
    """

    FILAS = 6
    COLUMNAS = 7

    def __init__(self):
        """Constructor.
        ---
        Inicializa el un tablero vacío.
        """
        super().__init__(TableroConectaCuatro.FILAS, TableroConectaCuatro.COLUMNAS)
