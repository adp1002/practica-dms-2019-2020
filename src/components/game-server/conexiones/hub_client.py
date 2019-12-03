import http.client
import os

class HubClient:
    """ Singleton REST client to interact with the hub server.
    ---
    This class is responsible of interfacing the hub server as another 
    data source, via a REST API presentation layer in the hub server.

    Note: Uses the HUB_SERVER_HOST and HUB_SERVER_PORT environment variables to 
    open the connection.
    """

    __instance = None

    def __init__(self):
        """ Constructor method.
        ---
        Do NOT use this method. Use instance() instead.
        """
        if (HubClient.__instance is not None):
            raise Exception('A singleton class cannot be initialized twice')
        self.__connection = http.client.HTTPConnection(os.getenv('HUB_SERVER_HOST', '127.0.0.1'), os.getenv('HUB_SERVER_PORT', 4567))

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

    def register(self, game, host, port):
        self.__connection.request('POST', '/server/register', headers = {'Content-Type': 'application/x-www-form-urlencoded'},
                                 body = 'name={}&host={}&port={}'.format(game, host, port))
        
        response = self.__connection.getresponse()
        return response.status == 200

