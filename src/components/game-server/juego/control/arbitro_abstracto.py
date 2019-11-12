from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):

    def __init__(self, tablero):
        self._tablero = tablero

    def es_valido(self, x, y):
        return self._tablero.obtener_pieza(x, y) != None

    @abstractmethod
    def hay_ganador(self):
        pass
