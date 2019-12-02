from juego.fabrica_abstracta_arbitro import FabricaAbstractaArbitro
from juego.logica.arbitro_conecta_cuatro import ArbitroConectaCuatro

class FabricaArbitroConectaCuatro(FabricaAbstractaArbitro):
    """ Fabrica de árbitros del conecta 4.
    ---
    La clase es una fabrica de creación de árbitros del conecta 4.
    """

    def crear_arbitro(self, tablero):
        """ Método que crea un arbitro del conecta 4 asociado a un tablero.
        ---
        Returns:
            Un árbitro del conecta 4.
        """
        return ArbitroConectaCuatro(tablero)