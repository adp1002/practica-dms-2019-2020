from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):
    """ Arbitro abstracto.
    ---
    La clase contiene las reglas del juego.
    """

    def __init__(self, tablero):
        """ Constructor.
        ---
        Inicializa un arbitro con el tablero de la partida.

        Parametros:
            - tablero: tablero de la partida.
        """
        self._tablero = tablero

    def es_valido(self, x, y):
        """ Método que comprueba si la jugada es válida.
        ---
        Parametros:
            - x: Fila del tablero.
            - y: Columna del tablero.
        Returns:
            True si es valido, sino False.
        """
        return self._tablero.obtener_pieza(x, y) is None and not self.esta_acabado()

    @abstractmethod
    def hay_ganador(self):
        """ Método que comprueba si existe un ganador.
        ---
        Returns:
            True si hay un ganador, sino False.
        """
        pass

    @abstractmethod
    def esta_acabado(self):
        """ Método que comprueba si la partida ha finalizado.
        ---
        Returns: 
            True si la partida ha terminado, sino False.
        """
        pass
