from juego.control.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

    def __init__(self, tablero):
        super(ArbitroTresRaya, self).__init__(tablero)

    def hay_ganador(self):
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
        return self.hay_ganador() || self._tablero.esta_lleno()
