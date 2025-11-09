'''
EJERCICIO
   ------------
   - id_ejercicio: int
   - nombre: str
   - tipo: str (CARDIO, FUERZA, FLEXIBILIDAD, MUSCULACION)
   - grupo_muscular: str
   - calorias_por_minuto: float
   - descripcion: str
   - instrucciones: str

'''
class Ejercicio:
    def __init__(self, id_ejercicio, nombre, tipo, grupo_muscular, calorias_por_minuto, descripcion, instrucciones):
        self.__id_ejercicio = id_ejercicio
        self.__nombre = nombre
        self.__tipo = tipo
        self.__grupo_muscular = grupo_muscular
        self.__calorias_por_minuto = calorias_por_minuto
        self.__descripcion = descripcion
        self.__instrucciones = instrucciones

    ## Getters##############################################
    def get_id_ejercicio(self):
        return self.__id_ejercicio
    def get_nombre(self):
        return self.__nombre
    def get_tipo(self):
        return self.__tipo
    def get_grupo_muscular(self):
        return self.__grupo_muscular
    def get_calorias_por_minuto(self):
        return self.__calorias_por_minuto
    def get_descripcion(self):
        return self.__descripcion
    def get_instrucciones(self):
        return self.__instrucciones

    ## Setters##############################################
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def set_grupo_muscular(self, grupo_muscular):
        self.__grupo_muscular = grupo_muscular
    def set_calorias_por_minuto(self, calorias_por_minuto):
        self.__calorias_por_minuto = calorias_por_minuto
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_instrucciones(self, instrucciones):
        self.__instrucciones = instrucciones
        