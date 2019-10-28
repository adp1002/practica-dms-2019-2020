from abc import ABC, abstractmethod

class TableroAbstracto(ABC):
	""" Clase abstracta que repreasenta un tablero.
	---
	La clase propociona la estructura de una tablero.
	"""

	@abstractmethod
	def colocar(self, x, y, pieza):
		""" Método que coloca un pieza en las coordenadas.
		---
			Parámetros:
				- x: Fila del tablero.
				- y: Columna del tablero.
				- pieza: Pieza a colocar.
		"""
		pass
	
	@abstractmethod
	def obtener_pieza(self, x, y):
		""" Método que devuelva la pieza de las coordenadas.
		---
			Parametros:
				- x: Fila del tablero.
				- y: Columna del tablero.
			Returns:
				Pieza del tablero.
		"""
		pass
	
	@abstractmethod
	def esta_lleno(self):
		""" Método que comprueba si el tablero esta lleno.
		---
			Returns:
				True si el tablero esta lleno, sino False.
		"""
		pass

	