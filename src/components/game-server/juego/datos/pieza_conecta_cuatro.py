from juego.modelo.pieza_abstracta import PiezaAbstracta

class PiezaConectaCuatro(PiezaAbstracta):
    """ Pieza del conecta cuatro.
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
        return isinstance(other, PiezaConectaCuatro) and self._tipo == other._tipo
