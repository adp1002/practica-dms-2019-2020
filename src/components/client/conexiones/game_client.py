import http.client
import json

class GameClient:
    """ REST client para interactuar con el servidor de juego
    ---
    Esta es la clase responsable de interactuar con el servidor de juego via API REST
    como si fuera cualquier otra fuente de datos.

    Nota: Utiliza game_server_host y game_server_port para mantener abierta la conexion.
    """
    def __init__(self,game_server_host,game_server_port):
        """ Constructor.
        ---
        Parameters:
            - game_server_host: La direccion del servidor de juego al que se quere conectar
            - game_server_port: El puerto del servidor de juego al que se quere conectar
        """
        self.game_server_host = game_server_host
        self.game_server_port = game_server_port
        self.__connection = http.client.HTTPConnection(self.game_server_host, self.game_server_port)
    
    """ Registra al jugador en el servidor de juego de la clase
    ---
    Parameters:
        - token: El token de autentificacion del usuario que realiza la peticion
    Returns:
        True si se pudo registrar al usuario en el servidor, si no, False
    """
    def registrar_usuario_en_servidor(self,token):
        self.__connection.request('POST', '/juego/registrar', headers = {'Content-Type': 'application/x-www-form-urlencoded'}, body = 'token=' + token)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return True
        return False

    """ Obtiene si es el turno del jugador que realizo la peticion
    ---
    Parameters:
        - token: El token de autentificacion del usuario que realiza la peticion
    Returns:
        True si es el turno del jugador, False si no es el turno y None si ocurrio un error
    """
    def get_turno(self,token):
        self.__connection.request('GET', '/juego/turno', headers = {'Content-Type': 'application/x-www-form-urlencoded'}, body = 'token=' + token)
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
    
    """ Coloca una pieza del jugador que realiza la peticion en la posicion deseada
    ---
    Parameters:
        - token: El token de autentificacion del usuario que realiza la peticion
        - x: Eje x del tablero
        - y: Eje y del tablero
    Returns:
        True si la jugada se realizo con exito, si no, False.
    """
    def jugar(self, token, x, y):
        self.__connection.request('POST', '/juego/jugada', headers = {'Content-Type': 'application/x-www-form-urlencoded'},
            body = 'token=' + token + '&x=' + x + '&y=' + y)
        response = self.__connection.getresponse()
        if (response.status == 200):
            return True
        return False

    """ Devuelve el tablero actual
    ---
    Returns:
        JSON del tablero, o None si hubo algun problema.
    """
    def get_tablero(self):
        self.__connection.request('GET', '/juego/tablero', headers = {'Content-Type': 'application/x-www-form-urlencoded'})
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
    
    """ Devuelve si la partida esta acabada
    ---
    Returns:
        True si la partida esta acabada, False si no esta acabada y None si hubo algun problema.
    """
    def esta_acabado(self):
        self.__connection.request('GET', '/juego/acabado', headers = {'Content-Type': 'application/x-www-form-urlencoded'})
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
    
    """ Devuelve el resultado de la partida, el cual depende del jugador que ha realizado la peticion
    ---
    Parameters:
        - token: El token de autentificacion del usuario que realiza la peticion
    Returns:
        El resultado del jugador ('Ganador', 'Perdedor' o 'Empate'), o None si hubo algun problema.
    """
    def get_resultado(self,token):
        self.__connection.request('GET', '/juego/turno', headers = {'Content-Type': 'application/x-www-form-urlencoded'}, body = 'token=' + token)
        response = self.__connection.getresponse()
        if (response.status == 200):
            response_string = response.read().decode('utf-8')
            return json.loads(response_string)
        return None
    

