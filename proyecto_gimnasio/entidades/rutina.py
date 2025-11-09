'''
RUTINA
   ------------
   - id_rutina: int
   - nombre: str
   - objetivo: str (BAJAR_PESO, GANAR_MUSCULO, etc.)
   - nivel: str	(principiante, intermedio, avanzado)
   - fecha_creacion: datetime
   - ejercicios: list[EjercicioRutina]  # Composición con duración específica
   
   + agregar_ejercicio(ejercicio: Ejercicio, duracion: int)
   + eliminar_ejercicio(id_ejercicio: int)
   + calcular_calorias_totales() -> float
'''
class Rutina:
    def __init__(self, id_rutina, nombre, objetivo, nivel, fecha_creacion):
        self.__id_rutina = id_rutina
        self.__nombre = nombre
        self.__objetivo = objetivo
        self.__nivel = nivel
        self.__fecha_creacion = fecha_creacion
        self.__ejercicios = []  # Lista de EjercicioRutina
# region getters y setters
    ## Getters##############################################
    def get_id_rutina(self):
        return self.__id_rutina
    def get_nombre(self):
        return self.__nombre
    def get_objetivo(self):
        return self.__objetivo
    def get_nivel(self):
        return self.__nivel
    def get_fecha_creacion(self):
        return self.__fecha_creacion
    def get_ejercicios(self):
        return self.__ejercicios
    ## setters########################################
    def set_nombre(self, nombre):
        self.__nombre = nombre  
    def set_objetivo(self, objetivo):
        self.__objetivo = objetivo
    def set_nivel(self, nivel):
        self.__nivel = nivel
    def set_fecha_creacion(self, fecha_creacion):
        self.__fecha_creacion = fecha_creacion
# endregion    

# region métodos

    # Métodos para agregar y eliminar ejercicios
    def agregar_ejercicio(self, ejercicio_rutina):
        self.__ejercicios.append(ejercicio_rutina)

    def eliminar_ejercicio(self, id_ejercicio):
        self.__ejercicios = [er for er in self.__ejercicios if er.get_ejercicio().get_id_ejercicio() != id_ejercicio]
    def calcular_calorias_totales(self):
        total_calorias = 0.0
        for ejercicio_rutina in self.__ejercicios:
            ejercicio = ejercicio_rutina.get_ejercicio()
            duracion = ejercicio_rutina.get_duracion()
            calorias_por_minuto = ejercicio.get_calorias_por_minuto()
            total_calorias += calorias_por_minuto * duracion
        return total_calorias   
#-----------------------------------------------------
# endregion