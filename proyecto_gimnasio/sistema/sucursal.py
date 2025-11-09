'''
SUCURSAL (Para grafo - entrega 3)
    ------------
    - id_sucursal: int
    - nombre: str
    - direccion: str
    - telefono: str
    - horario_apertura: time
    - horario_cierre: time
    - clases: list[ClaseGimnasio]
'''
class Sucursal:
    def __init__(self, id_sucursal, nombre, direccion, telefono, horario_apertura, horario_cierre):
        self.__id_sucursal = id_sucursal
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__horario_apertura = horario_apertura
        self.__horario_cierre = horario_cierre
        self.__clases = []

    ## Getters##############################################
    def get_id_sucursal(self):
        return self.__id_sucursal
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    def get_horario_apertura(self):
        return self.__horario_apertura
    def get_horario_cierre(self):
        return self.__horario_cierre
    def get_clases(self):
        return self.__clases

    ## Setters##############################################
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_direccion(self, direccion):
        self.__direccion = direccion
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_horario_apertura(self, horario_apertura):
        self.__horario_apertura = horario_apertura
    def set_horario_cierre(self, horario_cierre):
        self.__horario_cierre = horario_cierre
    
    #