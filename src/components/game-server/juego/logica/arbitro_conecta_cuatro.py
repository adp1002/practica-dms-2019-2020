from juego.logica.arbitro_abstracto import ArbitroAbstracto

class ArbitroConectaCuatro(ArbitroAbstracto):
    """ Arbitro del conecta cuatro.
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

    def es_valido(self, x, y):
        """ Método que comprueba si la jugada es válida.
        ---
        Parametros:
            - x: Fila del tablero.
            - y: Columna del tablero.
        Returns:
            True si es valido, sino False.
        """
        if x == 0:
            return super().es_valido(x, y)
        else:
            return super().es_valido(x, y) and self._tablero.obtener_pieza(x, y-1) is not None

    def hay_ganador(self):
        """ Método que comprueba si existe un ganador.
        ---
        Returns:
            True si hay un ganador, sino False.
        """
        t = self._tablero.obtener_array()
        for i in range(len(t)):
            for j in range(len(t[0])-3):
                if t[i][j] == t[i][j+1] == t[i][j+2] == t[i][j+3] != None:
                    return True

        for i in range(len(t[0])):
            for j in range(len(t)-3):
                if t[i][j] == t[i][j+1] == t[i][j+2] == t[i][j+3] != None:
                    return True

        for i in range(len(t[0])-3):
            for j in range(len(t)-3-1, -1, -1):
                if t[i][j] == t[i+1][j-1] == t[i+2][j-2] == t[i+3][j-3] != None:
                    return True

        for i in range(len(t[0])-3-1, -1, -1):
            for j in range(len(t)-3-1, -1, -1):
                if t[i+2][j-2] == t[i-1][j-1] == \
                t[i-2][j-2] == t[i-3][j-3] != None:
                    return True
        return False

    def esta_acabado(self):
        """ Método que comprueba si la partida ha finalizado.
        ---
        Returns:
            True si la partida ha terminado, sino False.
        """
        return self.hay_ganador() or self._tablero.esta_lleno()
