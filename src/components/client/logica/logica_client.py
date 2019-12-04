from conexiones.auth_client import AuthClient
from conexiones.hub_client import HubClient
from conexiones.game_client import GameClient


"""
Clase LogicaCliente es un clase con metodos estaticos.
Es la clase que lleva la logica y la que se comunica con la capa de datos.
"""

class LogicaCliente:
    """ Registra al usuario actual en el servidor
    ---
    Parameters:
        - username: Nombre del usuario a registrar
        - password: Contraseña del usuario a registrar
    Returns:
        True si el jugador se ha registrado correctamente, si no, False.
    """
    @staticmethod
    def registrar_usuario(username,password):
        return AuthClient.instance().registrar(username,password)


    """ Loguea al usuario actual
    ---
    Parameters:
        - username: Nombre del usuario a loguear
        - password: Contraseña del usuario a loguear
    Returns:
        El token de validacion del usuario en caso de que se haya logueado corectamente, si no, None.
    """
    @staticmethod
    def loguear_usuario(username,password):
        token = AuthClient.instance().login(username,password)
        return token


    """ Obtiene la lista de servidores
    ---
    Returns:
        Un array con la información del servidor escogido
    """
    @staticmethod
    def obtener_servidores(token):
        return HubClient.instance().get_servers(token)


    """ Registra al usuario del token en el servidor pasado por parametro
    ---
    Parameters:
        - token: El token del usuario que realiza la petición
        - servidor_seleccionado: El servidor seleccionado para registrar al usuario
    Returns:
        El servidor de juego en el que se ha registrado el jugador, None si ha surgido un error.
    """
    @staticmethod
    def registrarse_en_servidor(token,servidor_seleccionado):
        servidor_de_juego = GameClient(servidor_seleccionado['host'],servidor_seleccionado['port'])
        if((servidor_de_juego is None) or (not servidor_de_juego.registrar_usuario_en_servidor(token))):
            print('\nHa ocurrido un error al intentar entrar al servidor. Intenta probar en un nuevo servidor.\n')
            return None
        else:
            return servidor_de_juego


    """ Mantiene el curso de la partida de un jugador
    ---
    Parameters:
        - token: El token del usuario que va a jugar
        - servidor_seleccionado: el servidor seleccionado en el que va a jugando el usuario
        - x: Coordenada X donde poner la pieza
        - token: Coordenda Y donde poner la pieza
    Returns:
        El servidor de juego en el que se ha registrado el jugador, None si ha surgido un error.
    """
    @staticmethod
    def realizar_jugada(token,servidor_de_juego,x,y):
        se_ha_realizado_jugada = servidor_de_juego.jugar(token,x,y)
        return se_ha_realizado_jugada


    """ Manda la señal de que el usuario ha finalizado la partida
    ---
    Parameters:
        - token: El token del usuario que va a jugar
        - servidor_seleccionado: el servidor seleccionado en el que va a jugando el usuario
    Returns:
        True si el servidor ha recibido la petición, si no, False.
    """
    @staticmethod
    def finalizar_partida(token,servidor_seleccionado):
        return servidor_seleccionado.finalizar_partida(token)

    """ Obtiene el score actual
    ---
    Returns:
        El score actual
    """
    @staticmethod
    def get_score():
        return AuthClient.instance().get_score()