from juego.fabrica_abstracta_juegos import FabricaJuegoMesa
from tres_raya.modelo.pieza_tres_raya import PiezaTresRaya
from tres_raya.modelo.tablero_tres_raya import TableroTresRaya
from tres_raya.control.arbitro_tres_raya import ArbitroTresRaya

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
