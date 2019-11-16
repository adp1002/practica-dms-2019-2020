from juego.fabrica_abstracta_arbitro import FabricaAbstractaArbitro
from tres_raya.control.arbitro_tres_raya import ArbitroTresRaya

class FabricaArbitroTresRaya(FabricaAbstractaArbitro):
    """ Fabrica de árbitros del tres en rata.
    ---
    La clase es una fabrica de creación de árbitros del tres en raya.
    """

    def crear_arbitro(self, tablero):
        """ Método que crea un arbitro del tres en raya asociado a un tablero.
        ---
        Returns:
            Un árbitro del tres en raya.
        """
        return ArbitroTresRaya(tablero)
