from juego.control.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

    def __init__(self, tablero):
        super(ArbitroTresRaya, self).__init__(tablero)

    def esta_acabado(self):
        t = self._tablero
        return super.esta_acabado() or \
        t.obtener_pieza(0,0) == t.obtener_pieza(0,1) == t.obtener_pieza(0,2) or \
        t.obtener_pieza(1,0) == t.obtener_pieza(1,1) == t.obtener_pieza(1,2) or \
        t.obtener_pieza(2,0) == t.obtener_pieza(2,1) == t.obtener_pieza(2,2) or \

        t.obtener_pieza(0,0) == t.obtener_pieza(1,0) == t.obtener_pieza(2,0) or \
        t.obtener_pieza(0,1) == t.obtener_pieza(1,1) == t.obtener_pieza(2,1) or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,2) == t.obtener_pieza(2,2) or \

        t.obtener_pieza(0,0) == t.obtener_pieza(1,1) == t.obtener_pieza(2,2) or \
        t.obtener_pieza(0,2) == t.obtener_pieza(1,1) == t.obtener_pieza(2,0)
