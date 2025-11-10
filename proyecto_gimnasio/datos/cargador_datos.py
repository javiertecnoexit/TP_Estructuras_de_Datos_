# datos/cargador_datos.py
import json
import os
from datetime import datetime
from entidades.socio import Socio
from entidades.clase_gimnasio import ClaseGimnasio
from entidades.rutina import Rutina
from entidades.ejercicio import Ejercicio
from entidades.reserva import Reserva
from entidades.pago import Pago
from entidades.asistencia import Asistencia
from entidades.instructor import Instructor
from entidades.membresia import Membresia
from sistema.sucursal import Sucursal

class CargadorDatos:
    def __init__(self, ruta_datos="proyecto_gimnasio\datos"):
        self.ruta_datos = ruta_datos
        self.datos_cargados = {}
        
    def cargar_todos_los_datos(self):
        """Carga todos los archivos JSON y devuelve un diccionario con los datos"""
        try:
            print("📂 CARGANDO DATOS DESDE ARCHIVOS JSON...")
            
            self.datos_cargados = {
                'socios': self.cargar_socios(),
                'clases': self.cargar_clases(),
                'ejercicios': self.cargar_ejercicios(),
                'instructores': self.cargar_instructores(),
                'membresias': self.cargar_membresias(),
                'pagos': self.cargar_pagos(),
                'reservas': self.cargar_reservas(),
                'rutinas_base': self.cargar_rutinas(),
                'asistencias': self.cargar_asistencias(),
                'sucursales': self.cargar_sucursales()
            }
            
            print("✅ TODOS LOS DATOS CARGADOS EXITOSAMENTE")
            return self.datos_cargados
            
        except Exception as e:
            print(f"❌ ERROR AL CARGAR DATOS: {e}")
            return {}
    
    def _leer_json(self, archivo):
        """Lee un archivo JSON y devuelve los datos"""
        ruta_completa = os.path.join(self.ruta_datos, archivo)
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Archivo no encontrado: {ruta_completa}")
            return []
        except json.JSONDecodeError as e:
            print(f"⚠️  Error en formato JSON {archivo}: {e}")
            return []
    
    def cargar_socios(self):
        """Carga los datos de socios desde JSON"""
        datos = self._leer_json("socios.json")
        socios = []
        
        for dato in datos:
            # Calcular nivel de actividad basado en últimas asistencias
            nivel_actividad = self._calcular_nivel_actividad(dato)
            
            socio_data = {
                'id': dato['id_socio'],
                'nombre': dato['nombre'],
                'documento': dato['documento'],
                'email': dato['email'],
                'telefono': dato['telefono'],
                'fecha_inscripcion': self._parsear_fecha(dato['fecha_inscripcion']),
                'tipo_membresia': dato['tipo_membresia'],
                'estado': dato['estado'],
                'sucursal_preferida': dato.get('sucursal_preferida', 1),
                'nivel_actividad': nivel_actividad,
                'historial_rutinas': dato.get('historial_rutinas', []),
                'reservas_activas': dato.get('reservas_activas', []),
                'ultima_asistencia': self._parsear_fecha(dato.get('ultima_asistencia'))
            }
            socios.append(socio_data)
        
        print(f"👥 {len(socios)} socios cargados")
        return socios
    
    def cargar_clases(self):
        """Carga los datos de clases desde JSON"""
        datos = self._leer_json("clases.json")
        clases = []
        
        for dato in datos:
            clase_data = {
                'id': dato['id_clase'],
                'nombre': dato['nombre'],
                'tipo': dato['tipo'],
                'horario': self._parsear_fecha(dato['horario_inicio']),
                'horario_fin': self._parsear_fecha(dato['horario_fin']),
                'cupo_maximo': dato['cupo_maximo'],
                'instructor': dato['instructor'],
                'dificultad': dato['dificultad'],
                'sala': dato['sala'],
                'sucursal': dato.get('sucursal', 1),
                'socios_inscritos': dato.get('socios_inscritos', []),
                'estado': dato.get('estado', 'CONFIRMADA')
            }
            clases.append(clase_data)
        
        print(f"📅 {len(clases)} clases cargadas")
        return clases
    
    def cargar_ejercicios(self):
        """Carga los datos de ejercicios desde JSON"""
        datos = self._leer_json("ejercicios.json")
        ejercicios = []
        
        for dato in datos:
            ejercicio_data = {
                'id': dato['id_ejercicio'],
                'nombre': dato['nombre'],
                'tipo': dato['tipo'],
                'grupo_muscular': dato.get('grupo_muscular', 'GENERAL'),
                'calorias_por_minuto': dato['calorias_por_minuto'],
                'descripcion': dato.get('descripcion', ''),
                'instrucciones': dato.get('instrucciones', '')
            }
            ejercicios.append(ejercicio_data)
        
        print(f"💪 {len(ejercicios)} ejercicios cargados")
        return ejercicios
    
    def cargar_instructores(self):
        """Carga los datos de instructores desde JSON"""
        datos = self._leer_json("instructores.json")
        instructores = []
        
        for dato in datos:
            instructor_data = {
                'id': dato['id_instructor'],
                'nombre': dato['nombre'],
                'especialidad': dato['especialidad'],
                'telefono': dato.get('telefono', ''),
                'email': dato.get('email', ''),
                'fecha_contratacion': self._parsear_fecha(dato.get('fecha_contratacion')),
                'sucursal_base': dato.get('sucursal_base', 1),
                'clases_asignadas': dato.get('clases_asignadas', []),
                'certificaciones': dato.get('certificaciones', [])
            }
            instructores.append(instructor_data)
        
        print(f"👨‍🏫 {len(instructores)} instructores cargados")
        return instructores
    
    def cargar_membresias(self):
        """Carga los datos de membresías desde JSON"""
        datos = self._leer_json("membresias.json")
        membresias = []
        
        for dato in datos:
            membresia_data = {
                'tipo': dato['tipo'],
                'precio_mensual': dato['precio_mensual'],
                'clases_semanales': dato['clases_semanales'],
                'acceso_sucursales': dato.get('acceso_sucursales', []),
                'beneficios': dato.get('beneficios', [])
            }
            membresias.append(membresia_data)
        
        print(f"🎫 {len(membresias)} tipos de membresía cargados")
        return membresias
    
    def cargar_pagos(self):
        """Carga los datos de pagos desde JSON"""
        datos = self._leer_json("pagos.json")
        pagos = []
        
        for dato in datos:
            pago_data = {
                'id': dato['id_pago'],
                'socio_id': dato['socio_id'],
                'monto': dato['monto'],
                'fecha_vencimiento': self._parsear_fecha(dato['fecha_vencimiento']),
                'fecha_pago': self._parsear_fecha(dato.get('fecha_pago')),
                'tipo': dato['tipo'],
                'estado': dato['estado']
            }
            pagos.append(pago_data)
        
        print(f"💰 {len(pagos)} pagos cargados")
        return pagos
    
    def cargar_reservas(self):
        """Carga los datos de reservas desde JSON"""
        datos = self._leer_json("reservas.json")
        reservas = []
        
        for dato in datos:
            reserva_data = {
                'id': dato['id_reserva'],
                'socio_id': dato['socio_id'],
                'clase_id': dato['clase_id'],
                'fecha_reserva': self._parsear_fecha(dato['fecha_reserva']),
                'estado': dato['estado'],
                'prioridad': dato.get('prioridad', 1)
            }
            reservas.append(reserva_data)
        
        print(f"📋 {len(reservas)} reservas cargadas")
        return reservas
    
    def cargar_rutinas(self):
        """Carga los datos de rutinas desde JSON"""
        datos = self._leer_json("rutinas.json")
        rutinas = []
        
        for dato in datos:
            rutina_data = {
                'id': dato['id_rutina'],
                'nombre': dato['nombre'],
                'objetivo': dato['objetivo'],
                'nivel': dato.get('nivel', 'INTERMEDIO'),
                'fecha_creacion': self._parsear_fecha(dato.get('fecha_creacion')),
                'ejercicios': dato.get('ejercicios', [])
            }
            rutinas.append(rutina_data)
        
        print(f"📊 {len(rutinas)} rutinas cargadas")
        return rutinas
    
    def cargar_asistencias(self):
        """Carga los datos de asistencias desde JSON"""
        datos = self._leer_json("asistencias.json")
        asistencias = []
        
        for dato in datos:
            asistencia_data = {
                'id': dato['id_asistencia'],
                'socio_id': dato['socio_id'],
                'clase_id': dato['clase_id'],
                'fecha': self._parsear_fecha(dato['fecha']),
                'puntuacion': dato.get('puntuacion', 0),
                'calorias_quemadas': dato.get('calorias_quemadas', 0)
            }
            asistencias.append(asistencia_data)
        
        print(f"✅ {len(asistencias)} asistencias cargadas")
        return asistencias
    
    def cargar_sucursales(self):
        """Carga los datos de sucursales desde JSON"""
        datos = self._leer_json("sucursales.json")
        sucursales = []
        
        for dato in datos:
            sucursal_data = {
                'id': dato['id_sucursal'],
                'nombre': dato['nombre'],
                'direccion': dato['direccion'],
                'telefono': dato.get('telefono', ''),
                'horario_apertura': dato.get('horario_apertura', '06:00'),
                'horario_cierre': dato.get('horario_cierre', '23:00'),
                'capacidad_maxima': dato.get('capacidad_maxima', 50),
                'servicios': dato.get('servicios', [])
            }
            sucursales.append(sucursal_data)
        
        print(f"📍 {len(sucursales)} sucursales cargadas")
        return sucursales
    
    def _parsear_fecha(self, fecha_str):
        """Convierte string de fecha a objeto datetime"""
        if not fecha_str:
            return None
        
        formatos = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%H:%M'
        ]
        
        for formato in formatos:
            try:
                return datetime.strptime(fecha_str, formato)
            except (ValueError, TypeError):
                continue
        
        print(f"⚠️  No se pudo parsear fecha: {fecha_str}")
        return None
    
    def _calcular_nivel_actividad(self, datos_socio):
        """Calcula el nivel de actividad basado en datos del socio"""
        # Lógica simple para determinar nivel de actividad
        # En un sistema real, esto sería más complejo
        if datos_socio.get('ultima_asistencia'):
            ultima_asistencia = self._parsear_fecha(datos_socio['ultima_asistencia'])
            if ultima_asistencia:
                dias_desde_ultima_visita = (datetime.now() - ultima_asistencia).days
                if dias_desde_ultima_visita <= 7:
                    return "ALTO"
                elif dias_desde_ultima_visita <= 30:
                    return "MEDIO"
        
        return "BAJO"

# Función de utilidad para crear datos de ejemplo si no existen
def crear_datos_ejemplo(ruta="datos/"):
    """Crea archivos JSON de ejemplo si no existen"""
    # Esta función puede expandirse para crear datos iniciales
    print("📝 Creando datos de ejemplo...")
    # Por ahora, asumimos que los archivos ya existen
    pass

if __name__ == "__main__":
    # Prueba del cargador
    cargador = CargadorDatos()
    datos = cargador.cargar_todos_los_datos()
    print(f"Total de datos cargados: {len(datos)} categorías")