'''
GIMNASIO (Sistema Principal)
   ------------
   - nombre: str
   - sucursales: list[Sucursal]
   - socios: list[Socio]
   - instructores: list[Instructor]
   - rutinas: list[Rutina]
   
   + registrar_socio(datos: dict) -> Socio
   + crear_clase(datos: dict) -> ClaseGimnasio
   + generar_reporte_ocupacion() -> dict
   + buscar_clases_disponibles(tipo: str, fecha: datetime) -> list
'''
class Gimnasio:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__sucursales = []
        self.__socios = []
        self.__instructores = []
        self.__rutinas = []

    ## Getters##############################################
    def get_nombre(self):
        return self.__nombre
    def get_sucursales(self):
        return self.__sucursales
    def get_socios(self):
        return self.__socios
    def get_instructores(self):
        return self.__instructores
    def get_rutinas(self):
        return self.__rutinas

    ## Setters##############################################
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_sucursales(self, sucursales):
        self.__sucursales = sucursales
    def set_socios(self, socios):
        self.__socios = socios
    def set_instructores(self, instructores):
        self.__instructores = instructores
    def set_rutinas(self, rutinas):
        self.__rutinas = rutinas
    
    ## Métodos##############################################
    # Métodos para registrar socios, crear clases, generar reportes, etc.
    def registrar_socio(self, datos):
        pass  # Implementar lógica para registrar un socio  
    def crear_clase(self, datos):
        pass  # Implementar lógica para crear una clase de gimnasio
    def generar_reporte_ocupacion(self):
        pass  # Implementar lógica para generar reporte de ocupación
    def buscar_clases_disponibles(self, tipo, fecha):
        pass  # Implementar lógica para buscar clases disponibles
    