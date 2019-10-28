from juego.modelo.pieza_abstracta import PiezaAbstracta

class PiezaTresRaya(PiezaAbstracta):

    def __init__(self, tipo):
        """Constructor.
        ---
            Parametros:
                - tipo: String del tipo de pieza.
        """
        self.tipo = tipo

    def obtener_tipo(self):
        """ Metodo para obtener al tipo de pieza.
        ---
            Return:
                Un String del tipo de pieza.
        """
        return self.tipo
    
    def __eq__(self, other):
        return isinstance(other, PiezaTresRaya) and self.tipo == other.tipo

    def __str__(self):
        return self.tipo
