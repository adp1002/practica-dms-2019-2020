from juego.modelo.tablero_abstracto import TableroAbstracto

class TableroConectaCuatro(TableroAbstracto):
    """ Clase que representa un tablero del tres en raya.
    ---
    La clase almacena las piezas del tres en raya.
    """

    def __init__(self, ancho, alto):
        """Constructor.
        ---
        Inicializa el un tablero vacío.
        """
        super().__init__(ancho, alto)
