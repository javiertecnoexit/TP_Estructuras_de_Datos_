'''
2. CLASE_GIMNASIO
   ------------
   - id_clase: int
   - nombre: str
   - tipo: str (YOGA, CROSSFIT, SPINNING, etc.)
   - horario_inicio: datetime
   - horario_fin: datetime
   - cupo_maximo: int
   - instructor: str
   - dificultad: str (BAJA, MEDIA, AVANZADO)
   - sala: str
   - socios_inscritos: list[Socio]
   
   + agregar_reserva(socio: Socio) -> bool
   + cancelar_reserva(socio: Socio)
   + cupos_disponibles() -> int
   + obtener_lista_asistencia() -> list
'''
class ClaseGimnasio:
    def __init__(self, id_clase, nombre, tipo, horario_inicio, horario_fin, cupo_maximo, instructor, dificultad, sala):
        self.__id_clase = id_clase
        self.__nombre = nombre
        self.__tipo = tipo
        self.__horario_inicio = horario_inicio
        self.__horario_fin = horario_fin
        self.__cupo_maximo = cupo_maximo
        self.__instructor = instructor
        self.__dificultad = dificultad
        self.__sala = sala
        self.__socios_inscritos = []    
# region getters y setters
## Getters##############################################
    def get_id_clase(self):
        return self.__id_clase  
    def get_nombre(self):
        return self.__nombre
    def get_tipo(self):
        return self.__tipo
    def get_horario_inicio(self):
        return self.__horario_inicio
    def get_horario_fin(self):
        return self.__horario_fin
    def get_cupo_maximo(self):
        return self.__cupo_maximo
    def get_instructor(self):
        return self.__instructor
    def get_dificultad(self):
        return self.__dificultad
    def get_sala(self):
        return self.__sala
    def get_socios_inscritos(self):
        return self.__socios_inscritos
    def return_asistencias(self):
        return self.__socios_inscritos
    def return_asistencias(self):
        return self.__socios_inscritos
    def get_asistencias(self):
        return self.__asistencias
#-------------------------------------------
# setters########################################
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_documento(self, documento):
        self.__documento = documento
    def set_email(self, email):
        self.__email = email
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_tipo_membresia(self, tipo_membresia):
        self.__tipo_membresia = tipo_membresia
    def set_estado(self, estado):
        self.__estado = estado
#-----------------------------------------------------
# endregion

# region métodos
# Métodos##############################################
    def agregar_reserva(self, socio):
        if len(self.__socios_inscritos) < self.__cupo_maximo:
            self.__socios_inscritos.append(socio)
            return True
        else:
            return False    
    def cancelar_reserva(self, socio):
        if socio in self.__socios_inscritos:
            self.__socios_inscritos.remove(socio)   

    def cupos_disponibles(self):
        return self.__cupo_maximo - len(self.__socios_inscritos)  
      
    def obtener_lista_asistencia(self):
        return self.__socios_inscritos

# endregion
