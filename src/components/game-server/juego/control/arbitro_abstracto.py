from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):

    def __init__(self, tablero):
        self.__tablero = tablero

    def es_valido(self, x, y):
        return self.__tablero.obtener_pieza(x, y) != None

    def esta_acabado(self):
        return self.__tablero.esta_lleno()
