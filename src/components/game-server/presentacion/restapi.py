from flask import Flask, escape, request, abort

from juego.partida import Partida
from juego.jugador import Jugador
from tres_raya.fabrica_tres_raya import FabricaTresRaya
from tres_raya.fabrica_arbitro_tres_raya import FabricaArbitroTresRaya

class RestApi():

    JUEGOS = {"TresRaya" : (FabricaTresRaya, FabricaArbitroTresRaya)}

    def __init__(self, tipo):
        fabrica_juego = RestApi.JUEGOS.get(tipo)[0]
        fabrica_arbitro = RestApi.JUEGOS.get(tipo)[1]
        self.__partida = Partida(fabrica_juego, fabrica_arbitro)

    def registrar_jugador(self, request):
        token = request.form['token']
        jugador = Jugador(token)
        if not self.__partida.registrar_jugador(jugador):
            return (500, 'Server error')
        return (200, 'OK')

    def comprobar_turno(self, request):
        token = request.form['token']
        if self.__partida.obtener_turno().obtener_token() == token:
            return (200, 'True')
        return (201, 'False')

    def realizar_jugada(self, request):
        x = int(request.form['x'])
        y = int(request.form['y'])
        self.__partida.jugar(x,y)
        return (200, 'OK')

