from juego.fabrica_abstracta_juegos import FabricaJuegoMesa

class Partida():
	"""docstring for ."""

	def __init__(self, fabrica_juego, jugador1, jugador2):
		""" Constructor.
		---
			Parámetros:
				- fabrica_juego: FabricaJuegoMesa
				- jugador1: Jugador 1.
				- jugador2: Jugador 2.
		"""
		self.__jugador1 = jugador1
		self.__jugador2 = jugador2
		self.__fabrica = fabrica_juego
		self.__tablero = fabrica_juego.crear_tablero()
		self.__piezas = fabrica_juego.crear_pieza()
		self.__turno = 0
		self.__ganador = None

	def jugar(self, x, y):
		""" Método que realiza un movimiento.
		---
			Parámetros:
				- x: Fila del tablero.
				- y: Columna del tablero.
		"""
		pass

	def obtener_ganador(self):
		""" Método que devuelve el ganador de la partida.
		---
			Returs:
				El Jugador con el ganador, si no hay ganador None
		"""
		return self.__ganador

	def esta_acabado(self):
		""" Método que decide si la partida ha terminado.
		---
			Returs:
				True si la partida esta terminada, sino False
		"""
		return self.__ganador != None

	def obtener_turno(self):
		""" Método que obtiene el jugador con el turno.
		---
			Returns:
				Jugador con el turno.
		"""
		return self.__jugador1 if self.__turno % 2 == 0 else self.__jugador2
