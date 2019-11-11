from abc import ABC, abstractmethod

class FabricaAbstractaArbitro(ABC):

    @abstractmethod
    def crear_arbitro(self, tablero):
        pass