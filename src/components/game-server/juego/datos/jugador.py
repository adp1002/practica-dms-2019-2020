class Jugador:
    """ Clase que representa un jugador de una partida.
    ---
    La clase almacena el token de autentificación y el tipo de pieza del jugador.
    """

    def __init__(self, token):
        """ Constructor.
        ---
        Parametros:
            - token: token de autentificación.
        """
        self.__tipo = None
        self.__token = token

    def establecer_tipo(self, tipo):
        """ Establece el tipo de pieza del jugador.
        Parametros:
            - tipo: String que representa el tipo.
        """
        self.__tipo = tipo

    def obtener_tipo(self):
        """ Devuelve el tipo de pieza del jugador.
        Returns:
            Un String que representa el tipo.
        """
        return self.__tipo

    def obtener_token(self):
        """ Devuelve el token del jugador.
        Returns:
            Un String con el token.
        """
        return self.__token

    def __eq__(self, otro):
        return isinstance(otro, Jugador) and self.__token == otro.__token
