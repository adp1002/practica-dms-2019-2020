from abc import ABC, abstractmethod

class PiezaAbstracta(ABC):
	""" Clase abstracta que repreasenta un pieza.
	---
	La clase propociona la estructura de una pieza.
	"""

	@abstractmethod
	def get_tipo(self):
		""" Metodo para obtener al tipo de pieza.
		---
		Returns:
			Un String del tipo de pieza.
		"""
		pass
	
	@abstractmethod
	def __eq__(self, other):
		pass

	@abstractmethod
	def __str__(self):
		pass