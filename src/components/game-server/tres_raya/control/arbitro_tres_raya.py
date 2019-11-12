from juego.control.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

    def __init__(self, tablero):
        """ Constructor
        ---
        Llama al constructor de la superclase.

        Parametros:
            - tablero: tablero de la partida.
        """
        super().__init__(tablero)

    def hay_ganador(self):
        """
        ---
        Comprueba si existe un ganador comprobando todas las posibles
        combinaciones ganadoras.

        Returns: True si hay un ganador, False en caso contrario.
        """
        t = self._tablero
        return \
        t.obtener_pieza(0,0) == t.obtener_pieza(0,1) == t.obtener_pieza(0,2) or \
        t.obtener_pieza(1,0) == t.obtener_pieza(1,1) == t.obtener_pieza(1,2) or \
        t.obtener_pieza(2,0) == t.obtener_pieza(2,1) == t.obtener_pieza(2,2) or \
        t.obtener_pieza(0,0) == t.obtener_pieza(1,0) == t.obtener_pieza(2,0) or \
        t.obtener_pieza(0,1) == t.obtener_pieza(1,1) == t.obtener_pieza(2,1) or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,2) == t.obtener_pieza(2,2) or \
        t.obtener_pieza(0,0) == t.obtener_pieza(1,1) == t.obtener_pieza(2,2) or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,1) == t.obtener_pieza(2,0)

    def esta_acabado(self):
        """
        ---
        Comprueba si la partida ha finalizado, sea porque hay un ganador o
        porque el tablero está lleno.

        Returns: True si la partida ha terminado, False en caso contrario.
        """
        return self.hay_ganador() or self._tablero.esta_lleno()
