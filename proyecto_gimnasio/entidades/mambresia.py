'''
MEMBRESIA
    ------------
    - tipo: str
    - precio_mensual: float
    - clases_semanales: int
    - acceso_sucursales: list[Sucursal]
    - beneficios: list[str]

'''
class Membresia:
    def __init__(self, tipo, precio_mensual, clases_semanales):
        self.__tipo = tipo
        self.__precio_mensual = precio_mensual
        self.__clases_semanales = clases_semanales
        self.__acceso_sucursales = []
        self.__beneficios = []

    ## Getters##############################################
    def get_tipo(self):
        return self.__tipo
    def get_precio_mensual(self):
        return self.__precio_mensual
    def get_clases_semanales(self):
        return self.__clases_semanales
    def get_acceso_sucursales(self):
        return self.__acceso_sucursales
    def get_beneficios(self):
        return self.__beneficios

    ## Setters##############################################
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def set_precio_mensual(self, precio_mensual):
        self.__precio_mensual = precio_mensual
    def set_clases_semanales(self, clases_semanales):
        self.__clases_semanales = clases_semanales