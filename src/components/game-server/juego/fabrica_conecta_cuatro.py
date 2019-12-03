from juego.fabrica_abstracta_juegos import FabricaJuegoMesa
from juego.datos.pieza_conecta_cuatro import PiezaConectaCuatro
from juego.datos.tablero_conecta_cuatro import TableroConectaCuatro
from juego.logica.arbitro_conecta_cuatro import ArbitroConectaCuatro

class FabricaConectaCuatro(FabricaJuegoMesa):
    """ Fabrica del conecta 4.
    ---
    La clase se encarga de crear tableros y piezas del conecta 4.
    """

    def crear_pieza(self, tipo):
        """ Método que crea una pieza de un tipo.
        ---
        Parametros:
            - tipo: Un String que representa el tipo de pieza.
        Returns:
            Una pieza del juego.
        """
        return PiezaConectaCuatro(tipo)

    def crear_tablero(self):
        """ Método que crea un tablero.
        ---
        Returns:
            Un tablero del juego.
        """
        return TableroConectaCuatro()
    
    def crear_arbitro(self, tablero):
        """ Método que crea un arbitro.
        ---
        Returns:
            Un arbitro del juego.
        """
        return ArbitroConectaCuatro(tablero)
