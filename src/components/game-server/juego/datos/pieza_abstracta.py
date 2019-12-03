from abc import ABC, abstractmethod

class PiezaAbstracta(ABC):
    """ Clase abstracta que representa un pieza.
    ---
    La clase proporciona la estructura de una pieza.
    """

    def __init__(self, tipo):
        """Constructor.
        ---
            Parámetros:
                - tipo: String del tipo de pieza.
        """
        self._tipo = tipo

    def obtener_tipo(self):
        """ Método para obtener al tipo de pieza.
        ---
            Return:
                Un String del tipo de pieza.
        """
        return self.__tipo

    @abstractmethod
    def __eq__(self, other):
        pass

    def __str__(self):
        return self.__tipo
