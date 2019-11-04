class Partida():
	"""docstring for ."""

	def __init__(self, fabrica):
		"""Constructor.
		---
			Parámetros:
				- tablero: tablero de la partida.
				- jugador1: Jugador 1.
				- jugador2: Jugador 2.
		"""
		self.__fabrica = fabrica
		self.__tablero = fabrica.crear_tablero()
		self.__jugador1 = jugador1
		self.__jugador2 = jugador2
		self.__piezas = fabrica.crear_piezas()
		self.__arbitro = fabrica.crear_arbitro()
		self.__turno = 0
		self.__acabado = False

	def jugar(self, x, y):
		"""Método que realiza un movimiento.
		---
			Parámetros:
				- x: Fila del tablero.
				- y: Columna del tablero.
		"""
		if self.es_valido(x,y):
			self.__tablero.colocar(x,y)

	def obtener_ganador(self):
		"""Método que decide si la partida ha terminado.
		---
			Returs:
				Un Jugador con el ganador.
		"""
		pass

	def obtener_turno(self):
		"""Método que obtiene el jugador con el turno.
		---
			Returns:
				Jugador con el turno.
		"""
		if self.__turno:
			return self.__jugador1
		else:
			return self.__jugador2
