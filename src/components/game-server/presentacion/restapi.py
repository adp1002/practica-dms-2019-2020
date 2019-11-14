from flask import Flask, escape, request, abort
from auth.auth_client import AuthClient

from juego.partida import Partida
from juego.jugador import Jugador
from tres_raya.fabrica_tres_raya import FabricaTresRaya
from tres_raya.fabrica_arbitro_tres_raya import FabricaArbitroTresRaya

import json

class RestApi:

    JUEGOS = {"TresRaya" : (FabricaTresRaya, FabricaArbitroTresRaya)}

    def __init__(self, tipo):
        fabrica_juego = RestApi.JUEGOS.get(tipo)[0]()
        fabrica_arbitro = RestApi.JUEGOS.get(tipo)[1]()
        self.__partida = Partida(fabrica_juego, fabrica_arbitro)

    def status(self, request):
        """ Status handler.
        ---
        Always returns a tuple with the 200 status code and an "OK" message.
        """
        return (200, 'OK')

    def registrar_jugador(self, request):
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')

        jugador = Jugador(token)
        if not self.__partida.registrar_jugador(jugador):
            return (500, 'Server error')

        return (200, 'OK')

    def comprobar_turno(self, request):
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')

        turno = self.__partida.obtener_turno().obtener_token() == token

        return (200, json.dumps(turno))

    def realizar_jugada(self, request):
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
        tablero = self.__partida.obtener_tablero().obtener_array()
        out = [[None if pieza is None else str(pieza) for pieza in x] for x in tablero]

        return (200, json.dumps(out))

    def esta_acabado(self, request):
        acabado = self.__partida.esta_acabado()
        return (200, json.dumps(acabado))

    def obtener_resultado(self, request):
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

    def obtener_puntos(self, request):
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')
        try:
            jugador1 = self.__partida.obtener_jugador1()
            jugador2 = self.__partida.obtener_jugador2()
            puntos = jugador1.obtener_puntos() if token == jugador1.obtener_token() \
                else jugador2.obtener_puntos()
            return (200, json.dumps(puntos))
        except:
            return (400, 'Bad Request')

    def sumar_puntos(self, request):
        token = request.form['token']
        auth = AuthClient.instance()
        if not auth.validate_token(token):
            return (401, 'Unauthorized')
        try:
            cantidad = int(request.form['cantidad'])
            jugador1 = self.__partida.obtener_jugador1()
            jugador2 = self.__partida.obtener_jugador2()
            jugador1.sumar_puntos(cantidad) if token == jugador1.obtener_token() else jugador2.sumar_puntos(cantidad)
            return (200, 'OK')
        except:
            return (400, 'Bad Request')
