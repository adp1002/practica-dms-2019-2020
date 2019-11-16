from juego.control.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):
    """ Arbitro del tres en raya.
    ---
    La clase contiene las reglas del juego del tres en raya.
    """

    def __init__(self, tablero):
        """ Constructor
        ---
        Llama al constructor de la superclase.

        Parametros:
            - tablero: tablero de la partida.
        """
        super().__init__(tablero)

    def hay_ganador(self):
        """ Método que comprueba si existe un ganador.
        ---
        Returns:
            True si hay un ganador, sino False.
        """
        t = self._tablero
        return \
        t.obtener_pieza(0,0) == t.obtener_pieza(0,1) == t.obtener_pieza(0,2) != None or \
        t.obtener_pieza(1,0) == t.obtener_pieza(1,1) == t.obtener_pieza(1,2) != None or \
        t.obtener_pieza(2,0) == t.obtener_pieza(2,1) == t.obtener_pieza(2,2) != None or \
        t.obtener_pieza(0,0) == t.obtener_pieza(1,0) == t.obtener_pieza(2,0) != None or \
        t.obtener_pieza(0,1) == t.obtener_pieza(1,1) == t.obtener_pieza(2,1) != None or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,2) == t.obtener_pieza(2,2) != None or \
        t.obtener_pieza(0,0) == t.obtener_pieza(1,1) == t.obtener_pieza(2,2) != None or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,1) == t.obtener_pieza(2,0) != None

    def esta_acabado(self):
        """ Método que comprueba si la partida ha finalizado.
        ---
        Returns: 
            True si la partida ha terminado, sino False.
        """
        return self.hay_ganador() or self._tablero.esta_lleno()
