from abc import ABC, abstractmethod

class FabricaJuegoMesa(ABC):

    @abstractmethod
    def crear_pieza(self):
        pass

    @abstractmethod
    def crear_tablero(self):
        pass

    @abstractmethod
    def crear_arbitro(self):
        pass
