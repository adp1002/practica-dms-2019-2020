class Jugador:

    def __init__(self, token):
        self.__tipo = None
        self.__token = token

    def establecer_tipo(self, tipo):
        self.__tipo = tipo

    def obtener_tipo(self):
        return self.__tipo

    def obtener_token(self):
        return self.__token

    def __eq__(self, otro):
        return isinstance(otro, Jugador) and self.__token == otro.__token
