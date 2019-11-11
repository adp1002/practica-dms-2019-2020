from juego.control.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

    def __init__(self, tablero):
        super(ArbitroTresRaya, self).__init__(tablero)

    def esta_acabado(self):

        if super.esta_acabado():
            return True

        