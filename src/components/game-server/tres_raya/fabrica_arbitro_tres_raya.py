from juego.fabrica_abstracta_arbitro import FabricaAbstractaArbitro
from tres_raya.control.arbitro_tres_raya import ArbitroTresRaya

class FabricaArbitroTresRaya(FabricaAbstractaArbitro):

    def crear_arbitro(self, tablero):
        return ArbitroTresRaya(tablero)
        