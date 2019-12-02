from abc import ABC, abstractmethod

class PiezaAbstracta(ABC):
    """ Clase abstracta que representa un pieza.
    ---
    La clase proporciona la estructura de una pieza.
    """

    @abstractmethod
    def obtener_tipo(self):
        """ Método para obtener el tipo de pieza.
        ---
        Returns:
            Un String del tipo de pieza.
        """
        pass
    
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass
