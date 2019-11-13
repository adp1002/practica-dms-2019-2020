from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):

    def __init__(self, tablero):
        """ Constructor
        ---
        Inicializa un arbitro con el tablero de la partida.

        Parametros:
            - tablero: tablero de la partida.
        """
        self._tablero = tablero

    def es_valido(self, x, y):
        """
        ---

        """
        return self._tablero.obtener_pieza(x, y) is None

    @abstractmethod
    def hay_ganador(self):
        pass
