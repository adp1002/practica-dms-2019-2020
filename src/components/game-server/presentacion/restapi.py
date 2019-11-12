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
        
        return (200, json.dumps({'turno' : turno}))

    def realizar_jugada(self, request):
        token = request.form['token']
        auth = AuthClient.instance()
        turno = self.__partida.obtener_turno()
        if not auth.validate_token(token) or turno.obtener_token() != token:
            return (401, 'Unauthorized')
        
        x = int(request.form['x'])
        y = int(request.form['y'])
        self.__partida.jugar(x,y)
        return (200, 'OK')

    def obtener_tablero(self, request):
        tablero = str(self.__partida.obtener_tablero())
        
        return (200, json.dumps({'tablero' : tablero}))
