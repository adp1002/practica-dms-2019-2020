from abc import ABC, abstractmethod

class PiezaAbstracta(ABC):

	@abstractmethod
	def get_tipo(self):
		pass
	
	@abstractmethod
	def __eq__(self, other):
		pass

	@abstractmethod
	def __str__(self):
		pass