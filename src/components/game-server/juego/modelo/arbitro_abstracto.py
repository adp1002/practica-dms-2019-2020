from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):
    """Clase abstracta que representa las reglas del juego.
    ---
    La clase proporciona la estructura de las reglas del juego.
    """



    @abstractmethod
    def es_valido(self, tablero, x, y):
        """Método que comprueba la jugada.
        ---
            Parámetros:
                - x: Fila del tablero.
                - y: Columna del tablero.
            Returns:
                True si el movimiento es válido, sino False.
        """
        pass
