from flask import Flask, escape, request, abort
from presentacion.restapi import RestApi

rest_api = RestApi('TresRaya')

app = Flask(__name__)

@app.route('/')
def status():
    """ Status handler. Useful to test whether the server is running or not.
    ---
    get:
        summary: Status handler.
        description: Status testing endpoing.
        responses:
            200:
                description: The server is running correctly.
    """
    (code, message) = rest_api.status(request)
    if (code == 200):
        return 'Running'
    else:
        abort(code)

@app.route('/juego/registrar', methods = ['POST'])
def registrar_jugador():
    (code, message) = rest_api.registrar_jugador(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/juego/turno', methods = ['GET'])
def comprobar_turno():
    (code, message) = rest_api.comprobar_turno(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/juego/jugada', methods = ['POST'])
def realizar_jugada():
    (code, message) = rest_api.realizar_jugada(request)
    if (code == 200):
        return message
    else:
        abort(code)

@app.route('/juego/tablero', methods = ['GET'])
def obtener_tablero():
    (code, message) = rest_api.obtener_tablero(request)
    if (code == 200):
        return message
    else:
        abort(code)
