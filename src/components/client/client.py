import os
import requests

class Jugador:

    def __init__(self):
        self.username = input('Introduce el nombre del usuario:\n')
        self.password = input('Introduce la contraseña del usuario:\n')
        self.auth_server = os.getenv('AUTH_SERVER_PORT', 1234)
        self.hub_server = os.getenv('HUB_SERVER_PORT', 4567)
        self.game_server = os.getenv('GAME_SERVER_PORT', 6789)
        self.token = None

        #Creamos el usuario con el APIREST
        data = {'username':self.username,'password':self.password}
        response = requests.post(url = 'http://172.10.1.10:' + str(self.auth_server) + '/user/create', data = data)

        if response.status_code == 500:
            #500: El usuario no pudo ser creado (probablemente por exister uno con el mismo nombre)
            print('\nEl usuario no pudo ser creado. Probando login...')
        else:
            print('\nUsuario creado con exito. Logeando...')

        #Probamos a logear al usuario
        self.login(data)

    def login(self,data):
        response = requests.post(url = 'http://172.10.1.10:' + str(self.auth_server) + '/user/login', data = data)

        if response.status_code == 200:
            '''200: El usuario se auntenticó con éxito.'''
            print('¡Login correcto!\n\n')
            self.token = response.content
        elif response.status_code == 401:
            print('Login incorrecto. Credenciales incorrectas')
        else:
            print('Login incorrecto. Error desconocido.')

    def get_token(self):
        return self.token
    
    def get_servers(self):
        data = {'token':self.token}
        response = requests.get(url = 'http://172.10.1.20:' + str(self.hub_server) + '/server', data = data)
        servidores = response.json()
        #Si no hay servidores retornamos
        if not len(servidores):
            print('¡No hay servidores de juego activos!')
            return -1
        for idx,servidor in enumerate(servidores):
            print(str(idx + 1) + ". " + servidor['name'] + " (" + servidor['host'] + ":" + servidor['port'] + ")")


jugador = Jugador()
#Si el jugador no tiene token es que no se ha logeado
if(jugador.get_token() is None):
    print('Abortando...')
else:
    print('Listando servidores activos...\n')
    #Bucle para pedir servidores
    while jugador.get_servers() is -1:
        letra = input('¿Quieres repetir la busqueda? (S/N):\n')
        if(not((letra == "S") or (letra == "s"))):
            exit()
