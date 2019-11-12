import os
import requests

class Jugador:

    def __init__():
        self.username = input('Introduce el nombre del usuario')
        self.password = input('Introduce la contraseña del usuario')
        self.auth_server = os.getenv('AUTH_SERVER_PORT', 1234)

        '''Creamos el usuario con el APIREST'''
        data = {'username':username,
            'password':password}
        response = request.post(url = auth_server + '/user/create', data = data)

        if response.status_code == 500:
            '''500: El usuario no pudo ser creado (probablemente por exister uno con el mismo nombre)'''
            print('Probando login...')

        '''Probamos a logear al usuario'''
        self.login()

    '''
    def conexion_servidor():
        while (true):
            input('Presiona una tecla para refresacar.')
    '''


    def login():
        response = request.post(url = auth_server + '/user/login', data = data)

        if response.status_code == 200:
            '''200: El usuario se auntenticó con éxito.'''
            print('Login correcto')
            data = response.json()
            self.token = data['token']
        else if response.status_code == 401:
            print('Login incorrecto. Credenciales incorrectas')
        else:
            print('Login incorrecto. Error desconocido.')

    def get_token():
        return self.token