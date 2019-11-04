from juego.modelo.arbitro_abstracto import ArbitroAbstracto

class ArbitroTresRaya(ArbitroAbstracto):

	def es_valido(self, x, y):
		"""Método que comprueba la jugada.
		---
			Parámetros:
				- x: Fila del tablero.
				- y: Columna del tablero.
			Returns:
				True si el movimiento es válido, sino False.
		"""
		return x >= 0 or y >= 0 or x <= 2 or y <= 2 \
			or self.__tablero.obtener_pieza(x,y) is None
