from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):
    """Clase abstracta que representa las reglas del juego.
    ---
    La clase proporciona la estructura de las reglas del juego.
    """

    @abstractmethod
    def jugar(self, x, y):
        """Método que realiza un movimiento.
        ---
            Parámetros:
                - x: Fila del tablero.
                - y: Columna del tablero.
        """
        pass

    @abstractmethod
    def es_valido(self, x, y):
        """Método que comprueba la jugada.
        ---
            Parámetros:
                - x: Fila del tablero.
                - y: Columna del tablero.
            Returns:
                True si el movimiento es válido, sino False.
        """
        pass

    @abstractmethod
    def obtener_ganador():
        """Método que decide si la partida ha terminado.
        ---
            Returs:
                Un Jugador con el ganador.
        """
        pass

    @abstractmethod
    def obtener_turno():
        """Método que obtiene el jugador con el turno.
        ---
            Returns:
                Jugador con el turno.
        """
        pass
