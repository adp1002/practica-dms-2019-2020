from abc import ABC, abstractmethod

class Tablero(ABC):

	@abstractmethod
	def colocar(self, x, y, pieza):
		pass
	
	@abstractmethod
	def obtener_pieza(self, x, y):
		pass
	
	@abstractmethod
	def esta_lleno(self):
		pass

	