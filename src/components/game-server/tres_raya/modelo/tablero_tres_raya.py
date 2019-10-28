from juego.modelo.tablero_abstracto import TableroAbstracto

class TableroTresRaya(TableroAbstracto):

    def __init__(self):
        self.__tablero = [[None, None, None], [None, None, None], [None, None, None]]
        self.__piezas = 0

	def colocar(self, x, y, pieza):
		self.__tablero[x][y] = pieza
        self.__piezas += 1
	
	def obtener_pieza(self, x, y):
		return self.__tablero[x][y]
	
	def esta_lleno(self):
		return self.__piezas == 9
