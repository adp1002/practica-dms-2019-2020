class Jugador:

    def __init__(self, token):
        self.__tipo = None
        self.__token = token
        self.__puntos = 0

    def establecer_tipo(self, tipo):
        self.__tipo = tipo

    def obtener_tipo(self):
        return self.__tipo

    def obtener_token(self):
        return self.__token

    def obtener_puntos(self):
        return self.__puntos

    def sumar_puntos(self, cantidad):
        self.__puntos += cantidad

    def __eq__(self, otro):
        return isinstance(otro, Jugador) and self.__token == otro.__token
