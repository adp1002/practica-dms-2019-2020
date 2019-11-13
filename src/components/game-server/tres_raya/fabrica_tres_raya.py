from juego.fabrica_abstracta_juegos import FabricaJuegoMesa
from tres_raya.modelo.pieza_tres_raya import PiezaTresRaya
from tres_raya.modelo.tablero_tres_raya import TableroTresRaya
from tres_raya.control.arbitro_tres_raya import ArbitroTresRaya

class FabricaTresRaya(FabricaJuegoMesa):

	def crear_pieza(self, tipo):
		return PiezaTresRaya(tipo)

	def crear_tablero(self):
		return TableroTresRaya()

	def crear_arbitro(self, tablero):
		return ArbitroTresRaya(tablero)
