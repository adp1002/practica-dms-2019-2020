import http.client
import json

class HubClient:
    """ Singleton REST client to interact with the authentication server.
    ---
    This class is responsible of interfacing the authentication server as another 
    data source, via a REST API presentation layer in the authentication server.

    Note: Uses the AUTH_SERVER_HOST and AUTH_SERVER_PORT environment variables to 
    open the connection.
    """
    HUB_SERVER_HOST = '172.10.1.20'
    HUB_SERVER_PORT = '4567'
    
    __instance = None

    def __init__(self):
        """ Constructor method.
        ---
        Do NOT use this method. Use instance() instead.
        """
        if (HubClient.__instance is not None):
            raise Exception('A singleton class cannot be initialized twice')
        self.__connection = http.client.HTTPConnection(HubClient.HUB_SERVER_HOST, HubClient.HUB_SERVER_PORT)

    @staticmethod
    def instance():
        """ Singleton instance access method.
        ---
        Do NOT use the constructor. Use this method instead.

        Returns:
            The singleton instance of this class.
        """
        if (HubClient.__instance is None):
            HubClient.__instance = HubClient()
        return HubClient.__instance

    def get_servers(self, token):
        """ Obtiene los servidores de juego activos
        ---
        Parameters:
            - token: El token de autentificacion del usuario que realiza la peticion
        Returns:
            El JSON con la lista de servidores, o None en caso de error.
        """
        self.__connection.request('GET', '/server', headers = {'Content-Type': 'application/x-www-form-urlencoded'}, body = 'token=' + token)
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
