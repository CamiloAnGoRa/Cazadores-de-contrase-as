""" Excepciones del juego """

class JuegoCazadorError(Exception):
    """ Manejo de excepciones del juego """


class EntradaNoNumericaError(JuegoCazadorError):
    """ Valores que no se pueden pasar a enteros """

    def __init__(self, valor_ingresado: str) -> None:
        self.valor_ingresado = valor_ingresado
        super().__init__(f"El valor ingresado '{valor_ingresado}' no es un numero valido. Favor digitar digitos")

class LongitudInvalidaError(JuegoCazadorError):
    """ La longitud solicitada se encuentra fuera de un rango permitido"""

    def __init__(self, longitud: int, minimo: int, maximo: int) -> None:
        self.longitud = longitud
        self.minimo = minimo
        self.maximo = maximo
        super().__init__(f"La longitud solicitada '{longitud}' es incorrecta. Esta debe estar en el rango de: [{minimo}, {maximo}]")

class ContraseñaInvalidadError(JuegoCazadorError):
    """ La contraseña no cumple con los requisitos """

    def __init__(self, contraseña: str, requisitos_fallidos: list[str]) -> None:
        self.contraseña = contraseña
        self.requisitos_fallidos = requisitos_fallidos
        detalle = ", ".join(requisitos_fallidos)
        super().__init__(f"La contraseña '{contraseña}' no cumple con los siguientes requisitos: {detalle}.")

