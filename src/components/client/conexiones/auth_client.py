import http.client
import json

class AuthClient:
    """ Singleton REST client to interact with the authentication server.
    ---
    This class is responsible of interfacing the authentication server as another 
    data source, via a REST API presentation layer in the authentication server.

    Note: Uses the AUTH_SERVER_HOST and AUTH_SERVER_PORT environment variables to 
    open the connection.
    """
    AUTH_SERVER_HOST = '172.10.1.10'
    AUTH_SERVER_PORT = '1234'
    
    __instance = None

    def __init__(self):
        """ Constructor method.
        ---
        Do NOT use this method. Use instance() instead.
        """
        if (AuthClient.__instance is not None):
            raise Exception('A singleton class cannot be initialized twice')
        self.__connection = http.client.HTTPConnection(AuthClient.AUTH_SERVER_HOST, AuthClient.AUTH_SERVER_PORT)

    @staticmethod
    def instance():
        """ Singleton instance access method.
        ---
        Do NOT use the constructor. Use this method instead.

        Returns:
            The singleton instance of this class.
        """
        if (AuthClient.__instance is None):
            AuthClient.__instance = AuthClient()
        return AuthClient.__instance

    def registrar(self, username, password):
        """ Registra al jugador en el servidor de auth
        ---
        Parameters:
            - username: El nombre del usuario a registrar
            - password: La contraseña del usuario a registrar
        Returns:
            True si el jugador se ha registrado correctamente, si no, False.
        """
        self.__connection.request('POST', '/user/create', headers = {'Content-Type': 'application/x-www-form-urlencoded'},
         body = 'username=' + username + '&password=' + password)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return True
        return False

    def login(self, username, password):
        """ Loguea al usuario en el servidor de auth
        ---
        Parameters:
            - username: El nombre del usuario a loguear
            - password: La contraseña del usuario a loguear
        Returns:
            El token de validacion del usuario en caso de que se haya logueado corectamente, si no, None.
        """
        self.__connection.request('POST', '/user/login', headers = {'Content-Type': 'application/x-www-form-urlencoded'},
            body = 'username=' + username + '&password=' + password)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return response.read().decode()
        return None
    
    def get_score(self):
        """ Devuelve la puntuacion guardada en el servidor de auth.
        ---
        Returns:
            Un JSON con la puntuacion, o None en caso de error.
        """
        self.__connection.request('GET', '/score', headers = {'Content-Type': 'application/x-www-form-urlencoded'})
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
