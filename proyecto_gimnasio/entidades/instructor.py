'''
INSTRUCTOR
    ------------
    - id_instructor: int
    - nombre: str
    - especialidad: str
    - telefono: str
    - email: str
    - clases_asignadas: list[ClaseGimnasio]
'''
class Instructor:
    def __init__(self, id_instructor, nombre, especialidad, telefono, email):
        self.__id_instructor = id_instructor
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__telefono = telefono
        self.__email = email
        self.__clases_asignadas = []

    ## Getters##############################################
    def get_id_instructor(self):
        return self.__id_instructor
    def get_nombre(self):
        return self.__nombre
    def get_especialidad(self):
        return self.__especialidad
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    def get_clases_asignadas(self):
        return self.__clases_asignadas

    ## Setters##############################################
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_email(self, email):
        self.__email = email

        