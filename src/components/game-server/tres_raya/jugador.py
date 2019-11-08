import requests

class Jugador:

    def __init__(self,username,password,auth_server):
        self.username = username
        self.password = password
        self.auth_server = auth_server

        '''Creamos el usuario con el APIREST'''
        data = {'username':username,
            'password':password}
        response = request.post(url = auth_server + '/user/create', data = data)

        if response.status_code == 500:
            '''500: El usuario no pudo ser creado (probablemente por exister uno con el mismo nombre)'''
            print('El usuario no pudo ser creado, probando login')

        '''Probamos a logear al usuario'''
        self.login()


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
