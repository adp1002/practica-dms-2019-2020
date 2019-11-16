from juego.modelo.pieza_abstracta import PiezaAbstracta

class PiezaTresRaya(PiezaAbstracta):
    """ Pieza del tres en raya.
    ---
    La clase contiene el tipo de pieza.
    """

    def __init__(self, tipo):
        """Constructor.
        ---
            Parámetros:
                - tipo: String del tipo de pieza.
        """
        self.__tipo = tipo

    def obtener_tipo(self):
        """ Método para obtener al tipo de pieza.
        ---
            Return:
                Un String del tipo de pieza.
        """
        return self.__tipo
    
    def __eq__(self, other):
        return isinstance(other, PiezaTresRaya) and self.__tipo == other.__tipo

    def __str__(self):
        return self.__tipo
