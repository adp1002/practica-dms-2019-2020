import http.client
import os

class AuthClient:
    """ Singleton REST client to interact with the authentication server.
    ---
    This class is responsible of interfacing the authentication server as another 
    data source, via a REST API presentation layer in the authentication server.

    Note: Uses the AUTH_SERVER_HOST and AUTH_SERVER_PORT environment variables to 
    open the connection.
    """

    __instance = None

    def __init__(self):
        """ Constructor method.
        ---
        Do NOT use this method. Use instance() instead.
        """
        if (AuthClient.__instance is not None):
            raise Exception('A singleton class cannot be initialized twice')
        self.__connection = http.client.HTTPConnection(os.getenv('AUTH_SERVER_HOST', '127.0.0.1'), os.getenv('AUTH_SERVER_PORT', 1234))

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

    def validate_token(self, token):
        """ Performs the token validation against the authentication server.
        ---
        Parameters:
            - token: The authentication token to validate.
        Returns:
            True if the token given is a valid session token in the authentication server. False otherwise.
        """
        self.__connection.request('GET', '/token/check', headers = {'Content-Type': 'application/x-www-form-urlencoded'}, body = 'token=' + token)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return True
        return False

    def add_score(self, token, score, won = 0, lost = 0):
        """ Performs the token validation against the authentication server.
        ---
        Parameters:
            - token: The authentication token to validate.
            - score: The score to add to the user.
            - won: Number of games that the player won.
            - lost: Number of games that the player lost.
        Returns:
            True if the token given is a valid session token in the authentication server. False otherwise.
        """
        self.__connection.request('GET', '/score/add', headers = {'Content-Type': 'application/x-www-form-urlencoded'},
            body = 'token=' + token + '&score=' + score + '&games_won=' + won + '&games_lost=' + lost)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return True
        return False
