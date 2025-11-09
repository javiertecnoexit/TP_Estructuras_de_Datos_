'''
EJERCICIO_RUTINA (Clase asociativa)
   ------------
   - ejercicio: Ejercicio
   - duracion_minutos: int
   - repeticiones: int
   - series: int
   
   + calcular_calorias_quemadas() -> float
'''
class EjercicioRutina:
    def __init__(self, ejercicio, duracion_minutos, repeticiones, series):
        self.__ejercicio = ejercicio
        self.__duracion_minutos = duracion_minutos
        self.__repeticiones = repeticiones
        self.__series = series

    ## Getters##############################################
    def get_ejercicio(self):
        return self.__ejercicio
    def get_duracion(self):
        return self.__duracion_minutos
    def get_repeticiones(self):
        return self.__repeticiones
    def get_series(self):
        return self.__series

    ## Setters##############################################
    def set_duracion(self, duracion_minutos):
        self.__duracion_minutos = duracion_minutos
    def set_repeticiones(self, repeticiones):
        self.__repeticiones = repeticiones
    def set_series(self, series):
        self.__series = series

    # Método para calcular las calorías quemadas en este ejercicio de la rutina
    def calcular_calorias_quemadas(self):
        calorias_por_minuto = self.__ejercicio.get_calorias_por_minuto()
        return calorias_por_minuto * self.__duracion_minutos