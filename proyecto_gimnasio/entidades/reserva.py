'''
RESERVA
   ------------
   - id_reserva: int
   - socio: Socio
   - clase: ClaseGimnasio
   - fecha_reserva: datetime
   - fecha_clase: datetime
   - estado: str (CONFIRMADA, CANCELADA, EN_ESPERA)
   - prioridad: int  # Para cola de prioridad (entrega 3)
   
   + confirmar()
   + cancelar()
'''
class Reserva:
    def __init__(self, id_reserva, socio, clase, fecha_reserva, fecha_clase, estado, prioridad):
        self.__id_reserva = id_reserva
        self.__socio = socio
        self.__clase = clase
        self.__fecha_reserva = fecha_reserva
        self.__fecha_clase = fecha_clase
        self.__estado = estado
        self.__prioridad = prioridad

    ## Getters##############################################
    def get_id_reserva(self):
        return self.__id_reserva
    def get_socio(self):
        return self.__socio
    def get_clase(self):
        return self.__clase
    def get_fecha_reserva(self):
        return self.__fecha_reserva
    def get_fecha_clase(self):
        return self.__fecha_clase
    def get_estado(self):
        return self.__estado
    def get_prioridad(self):
        return self.__prioridad

    ## Setters##############################################
    def set_socio(self, socio):
        self.__socio = socio
    def set_clase(self, clase):
        self.__clase = clase
    def set_fecha_reserva(self, fecha_reserva):
        self.__fecha_reserva = fecha_reserva
    def set_fecha_clase(self, fecha_clase):
        self.__fecha_clase = fecha_clase
    def set_estado(self, estado):
        self.__estado = estado
    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    # Métodos para confirmar y cancelar la reserva
    def confirmar(self):
        self.__estado = "CONFIRMADA"

    def cancelar(self):
        self.__estado = "CANCELADA"