'''
 ASISTENCIA
   ------------
   - id_asistencia: int
   - socio: Socio
   - clase: ClaseGimnasio
   - fecha: datetime
   - llego_tarde: bool
   - calorias_quemadas: float

'''
class Asistencia:
    def __init__(self, id_asistencia, socio, clase, fecha, llego_tarde, calorias_quemadas):
        self.__id_asistencia = id_asistencia
        self.__socio = socio
        self.__clase = clase
        self.__fecha = fecha
        self.__llego_tarde = llego_tarde
        self.__calorias_quemadas = calorias_quemadas

    ## Getters##############################################
    def get_id_asistencia(self):
        return self.__id_asistencia
    def get_socio(self):
        return self.__socio
    def get_clase(self):
        return self.__clase
    def get_fecha(self):
        return self.__fecha
    def get_llego_tarde(self):
        return self.__llego_tarde
    def get_calorias_quemadas(self):
        return self.__calorias_quemadas

    ## Setters##############################################
    def set_socio(self, socio):
        self.__socio = socio
    def set_clase(self, clase):
        self.__clase = clase
    def set_fecha(self, fecha):
        self.__fecha = fecha
    def set_llego_tarde(self, llego_tarde):
        self.__llego_tarde = llego_tarde
    def set_calorias_quemadas(self, calorias_quemadas):
        self.__calorias_quemadas = calorias_quemadas

        