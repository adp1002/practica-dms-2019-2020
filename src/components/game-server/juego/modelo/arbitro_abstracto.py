from abc import ABC, abstractmethod

class ArbitroAbstracto(ABC):

	@abstractmethod
	def jugar(self, x, y):
		pass
	
	@abstractmethod
	def es_valido(self, x, y):
		pass
	