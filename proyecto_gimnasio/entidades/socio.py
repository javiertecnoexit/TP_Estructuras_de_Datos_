'''
CLASES PRINCIPALES:

1. SOCIO
   ------------
   - id_socio: int
   - nombre: str
   - documento: str
   - email: str
   - telefono: str
   - fecha_inscripcion: datetime
   - tipo_membresia: str (BASICA, PREMIUM, VIP)
   - estado: str (ACTIVO, INACTIVO, SUSPENDIDO)
   - historial_rutinas: list[Rutina]
   - reservas_activas: list[Reserva]
   - pagos: list[Pago]
   - asistencias: list[Asistencia]
   
   + calcular_calorias_totales() -> float
   + obtener_progreso() -> dict
   + puede_reservar() -> bool
   + renovar_membresia()
   + agregar_asistencia(clase: ClaseGimnasio)
'''

class Socio:
    def __init__(self, id_socio, nombre, documento, email, telefono, fecha_inscripcion, tipo_membresia, estado):
        self.__id_socio = id_socio
        self.__nombre = nombre
        self.__documento = documento
        self.__email = email
        self.__telefono = telefono
        self.__fecha_inscripcion = fecha_inscripcion
        self.__tipo_membresia = tipo_membresia
        self.__estado = estado
        self.__historial_rutinas = []
        self.__reservas_activas = []
        self.__pagos = []
        self.__asistencias = []

## Getters##############################################
    def get_id_socio(self):
        return self.__id_socio
    def get_nombre(self):
        return self.__nombre
    def get_documento(self):
        return self.__documento
    def get_email(self):
        return self.__email
    def get_telefono(self):
        return self.__telefono
    def get_fecha_inscripcion(self):
        return self.__fecha_inscripcion
    def get_tipo_membresia(self):
        return self.__tipo_membresia
    def get_estado(self):
        return self.__estado
    def get_historial_rutinas(self):
        return self.__historial_rutinas
    def get_reservas_activas(self):
        return self.__reservas_activas
    def get_pagos(self):
        return self.__pagos
    def get_asistencias(self):
        return self.__asistencias
#-----------------------------------------------------

# Setters##############################################
# no todos los atributos deben tener setters,
# por ejemplo id_socio y fecha_inscripcion no deben modificarse, entre otros.
    
    
    def set_email(self, email):
        self.__email = email
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_tipo_membresia(self, tipo_membresia):
        self.__tipo_membresia = tipo_membresia
    def set_estado(self, estado):
        self.__estado = estado  
   
    def set_reservas_activas(self, reservas_activas):
        self.__reservas_activas = reservas_activas
   
    
#-----------------------------------------------------

    def calcular_calorias_totales(self):
        total_calorias = sum(rutina.calorias_quemadas for rutina in self.historial_rutinas)
        return total_calorias

    def obtener_progreso(self):
        progreso = {}
        for rutina in self.historial_rutinas:
            progreso[rutina.nombre] = {
                'sesiones_completadas': rutina.sesiones_completadas,
                'objetivo_sesiones': rutina.objetivo_sesiones
            }
        return progreso

    def puede_reservar(self):
        return self.estado == 'ACTIVO' and len(self.reservas_activas) < 5

    def renovar_membresia(self):
        # Lógica para renovar la membresía del socio
        pass

    def agregar_asistencia(self, clase):
        self.asistencias.append(clase)