from juego.datos.pieza_abstracta import PiezaAbstracta

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
        super().__init__(tipo)

    def __eq__(self, other):
        return isinstance(other, PiezaTresRaya) and self.__tipo == other.__tipo
