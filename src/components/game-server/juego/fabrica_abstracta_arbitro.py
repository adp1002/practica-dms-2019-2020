from abc import ABC, abstractmethod

class FabricaAbstractaArbitro(ABC):
    """ Fabrica abstracta de árbitros.
    ---
    La clase es una fabrica abstracta de creación de árbitros.
    """

    @abstractmethod
    def crear_arbitro(self, tablero):
        """ Método que crea un arbitro asociado a un tablero.
        ---
        Returns:
            Un árbitro.
        """
        pass
