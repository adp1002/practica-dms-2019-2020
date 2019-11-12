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
