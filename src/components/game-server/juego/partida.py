from juego.fabrica_abstracta_juegos import FabricaJuegoMesa

class Partida:
	"""docstring for ."""

	def __init__(self, fabrica_juego, fabrica_arbitro):
		""" Constructor.
		---
			Parámetros:
				- fabrica_juego: FabricaJuegoMesa
				- jugador1: Jugador 1.
				- jugador2: Jugador 2.
		"""
		self.__jugador1 = None
		self.__jugador2 = None
		self.__fabrica = fabrica_juego
		self.__tablero = fabrica_juego.crear_tablero()
		self.__turno = 0
		self.__ganador = None
		self.__arbitro = fabrica_arbitro.crear_arbitro(self.__tablero)

	def registrar_jugador(self, jugador):
		if self.__jugador1 is None:
			self.__jugador1 = jugador
			self.__jugador1.establecer_tipo('X')
		elif self.__jugador2 is None:
			self.__jugador2 = jugador
			self.__jugador2.establecer_tipo('O')
		else:
			return False
		return True
		
	def jugar(self, x, y):
		""" Método que realiza un movimiento.
		---
			Parámetros:
				- x: Fila del tablero.
				- y: Columna del tablero.
		"""
		if self.__arbitro.es_valido(x, y):
			self.__tablero.colocar(x, y,
				self.__fabrica.crear_pieza(self.obtener_turno().obtener_tipo()))
			self.__turno += 1
		else:
			raise

	def obtener_ganador(self):
		""" Método que devuelve el ganador de la partida.
		---
			Returs:
				El Jugador con el ganador, si no hay ganador None
		"""
		return self.obtener_turno() if self.__arbitro.hay_ganador() else None


	def esta_acabado(self):
		""" Método que decide si la partida ha terminado.
		---
			Returs:
				True si la partida esta terminada, sino False
		"""
		return self.__arbitro.esta_acabado()

	def obtener_turno(self):
		""" Método que obtiene el jugador con el turno.
		---
			Returns:
				Jugador con el turno.
		"""
		return self.__jugador1 if self.__turno % 2 == 0 else self.__jugador2

	def obtener_tablero(self):
		return self.__tablero