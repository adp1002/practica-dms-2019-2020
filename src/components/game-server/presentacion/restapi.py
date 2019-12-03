from flask import Flask, escape, request, abort
from auth.auth_client import AuthClient

from juego.partida import Partida
from juego.datos.jugador import Jugador
from juego.fabrica_tres_raya import FabricaTresRaya
#from juego.fabrica_conecta_cuatro import FabricaConectaCuatro

import json

class RestApi:
    """ Clase fachada de la API REST
    ---
    Esta clase es una fachada con las operaciones proporcionadas a través de la API REST.
    """

    JUEGOS = {"TresRaya" : FabricaTresRaya
              #"Conecta4" : FabricaConectaCuatro
             }

    def __init__(self, tipo):
        """ Constructor.
        ---
        Parametros:
            - tipo: String con el nombre del juego.
        """
        self.__fabrica_juego = RestApi.JUEGOS.get(tipo)()
        self.__partida = Partida(self.__fabrica_juego)
        self.__finalizar = False

    def status(self, request):
        """ Controlador de estado.
        ---
        Siempre devuelve una tupla con el código de estado 200 y un mensaje "OK".
        """
        return (200, 'OK')

    def registrar_jugador(self, request):
        """ Registra un jugador en la partida.
        ---
        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se ha registrado con éxito.
                - (401, 'Unauthorized') cuando el token es invalido.
                - (500, 'Server error') cuando la partida esta llena.
        """
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')

        jugador = Jugador(token)
        if not self.__partida.registrar_jugador(jugador):
            return (500, 'Server error')

        return (200, 'OK')

    def comprobar_turno(self, request):
        """ Comprueba el turno de un jugador.
        ---
        Devuelve True si el jugador tiene el turno, sino False.

        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, True o False) comprobación correcta.
                - (401, 'Unauthorized') cuando el token es invalido.
        """
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')

        turno = self.__partida.obtener_turno().obtener_token() == token

        return (200, json.dumps(turno))

    def realizar_jugada(self, request):
        """ Realiza una jugada en la partida.
        ---
        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se ha realizado con éxito.
                - (400, 'Bad Request') cuando las coordenadas son invalidas o la partida esta acabada.
                - (401, 'Unauthorized') cuando el token es invalido.
        """
        token = request.form['token']
        auth = AuthClient.instance()
        turno = self.__partida.obtener_turno()
        if not auth.validate_token(token) or turno.obtener_token() != token:
            return (401, 'Unauthorized')

        try:
            x = int(request.form['x'])
            y = int(request.form['y'])
            self.__partida.jugar(x,y)
            return (200, 'OK')
        except:
            return (400, 'Bad Request')

    def obtener_tablero(self, request):
        """ Devuelve el tablero en forma de matriz.
        ---
        El tablero esta en formato JSON.

        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, 'OK') cuando se ha devuelto con éxito.
        """
        tablero = self.__partida.obtener_tablero().obtener_array()
        out = [[None if pieza is None else str(pieza) for pieza in x] for x in tablero]

        return (200, json.dumps(out))

    def esta_acabado(self, request):
        """ Comprueba si la partida esta acabada.
        ---
        Devuelve True si la partida esta acabada, sino False.

        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, True o False) comprobación correcta.
        """
        acabado = self.__partida.esta_acabado()
        return (200, json.dumps(acabado))

    def obtener_resultado(self, request):
        """ Devuelve el resultado obtenido por el jugador.
        ---
        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, 'Ganador', 'Perdedor' o 'Empate') comprobación correcta.
                - (400, 'Bad Request') cuando la partida no esta acabada.
                - (401, 'Unauthorized') cuando el token es invalido.
        """
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')

        if not self.__partida.esta_acabado():
            return (400, 'Bad Request')

        ganador = self.__partida.obtener_ganador()

        if ganador is None:
            resultado = 'Empate'
        elif token == ganador.obtener_token():
            resultado = 'Ganador'
        else:
            resultado = 'Perdedor'
        
        return (200, resultado)

    def finalizar_partida(self, request):
        """ Finaliza la partide e inicializa otra cuando los dos clientes realizan esta petición.
        ---
        Parametros:
            - request: La solicitud HTTP recibida en el REST endpoint.
        Returns:
            Una tupla con los siguientes valores:
                - (200, 'OK') operación correcta.
                - (401, 'Unauthorized') cuando el token es invalido.
        """
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')
        
        if self.__finalizar:
            self.__partida = Partida(self.__fabrica_juego, self.__fabrica_arbitro)
            self.__finalizar = False
        else:
            ganador = self.__partida.obtener_ganador()
            perdedor = self.__partida.obtener_perdedor()
            if ganador is not None:
                auth.add_score(ganador.obtener_token(), 1, 1, 0)
                auth.add_score(perdedor.obtener_token(), -1, 0, 1)
            self.__finalizar = True
        
        return (200, 'OK')
