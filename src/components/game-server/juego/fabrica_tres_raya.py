from juego.fabrica_abstracta_juegos import FabricaJuegoMesa
from juego.datos.pieza_tres_raya import PiezaTresRaya
from juego.datos.tablero_tres_raya import TableroTresRaya
from juego.logica.arbitro_tres_raya import ArbitroTresRaya

class FabricaTresRaya(FabricaJuegoMesa):
    """ Fabrica del tres en rata.
    ---
    La clase se encarga de crear tableros y piezas del tres en raya.
    """

    def crear_pieza(self, tipo):
        """ Método que crea una pieza de un tipo.
        ---
        Parametros:
            - tipo: Un String que representa el tipo de pieza.
        Returns:
            Una pieza del juego.
        """
        return PiezaTresRaya(tipo)

    def crear_tablero(self):
        """ Método que crea un tablero.
        ---
        Returns:
            Un tablero del juego.
        """
        return TableroTresRaya()

    def crear_arbitro(self, tablero):
        """ Método que crea un arbitro.
        ---
        Returns:
            Un arbitro del juego.
        """
        return ArbitroTresRaya(tablero)