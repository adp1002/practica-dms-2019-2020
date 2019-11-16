from abc import ABC, abstractmethod

class FabricaJuegoMesa(ABC):
    """ Fabrica abstracta de juegos de mesa.
    ---
    La clase se encarga de crear tableros y piezas de un juego.
    """

    @abstractmethod
    def crear_pieza(self, tipo):
        """ Método que crea una pieza de un tipo.
        ---
        Parametros:
            - tipo: Un String que representa el tipo de pieza.
        Returns:
            Una pieza del juego.
        """
        pass

    @abstractmethod
    def crear_tablero(self):
        """ Método que crea un tablero.
        ---
        Returns:
            Un tablero del juego.
        """
        pass
