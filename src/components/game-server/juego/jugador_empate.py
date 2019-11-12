from juego.jugador import Jugador

class JugadorEmpate(Jugador):

    __instance = None

    def __init__(self):
        """ Constructor method.
        ---
        Do NOT use this method. Use instance() instead.
        """
        if (JugadorEmpate.__instance is not None):
            raise Exception('A singleton class cannot be initialized twice')
        super(JugadorEmpate, self).__init__(None)
    
    @staticmethod
    def instance():
        """ Singleton instance access method.
        ---
        Do NOT use the constructor. Use this method instead.

        Returns:
            The singleton instance of this class.
        """
        if (JugadorEmpate.__instance is None):
            JugadorEmpate.__instance = JugadorEmpate()
        return JugadorEmpate.__instance
