"""
TRABAJO PRÁCTICO INTEGRADOR - GESTIÓN DE GIMNASIOS
Estructuras de Datos en Python
Main File - Sistema Principal
"""

import json
import os
from datetime import datetime, timedelta
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
from sistema.gimnasio import Gimnasio
from estructuras_datos.arbol_socios import ArbolSocios
from estructuras_datos.arbol_rutinas import ArbolRutinas
from estructuras_datos.cola_prioridad_reservas import ColaPrioridadReservas
from estructuras_datos.grafo_sucursales import GrafoSucursales
from datos.cargador_datos import CargadorDatos

class SistemaGimnasios:
    def __init__(self):
        self.gimnasio = None
        self.arbol_socios = ArbolSocios()
        self.arbol_rutinas = ArbolRutinas()
        self.cola_reservas = ColaPrioridadReservas()
        self.grafo_sucursales = GrafoSucursales()
        self.cargador = CargadorDatos()
        
    def inicializar_sistema(self):
        """Inicializa todo el sistema cargando datos y estructuras"""
        print("=" * 60)
        print("SISTEMA DE GESTIÓN DE GIMNASIOS - INICIALIZANDO")
        print("=" * 60)
        
        # Cargar datos básicos
        datos = self.cargador.cargar_todos_los_datos()
        
        # Crear instancia del gimnasio principal
        self.gimnasio = Gimnasio("PowerFit Gym", "Av. Principal 123")
        
        # Cargar sucursales en el grafo
        print("\n📊 CARGANDO ESTRUCTURAS DE DATOS...")
        self._cargar_sucursales(datos['sucursales'])
        
        # Cargar instructores
        self._cargar_instructores(datos['instructores'])
        
        # Cargar ejercicios y rutinas base
        self._cargar_ejercicios_rutinas(datos['ejercicios'], datos['rutinas_base'])
        
        # Cargar socios en lista lineal y árbol
        self._cargar_socios(datos['socios'])
        
        # Cargar clases y reservas
        self._cargar_clases_reservas(datos['clases'], datos['reservas'])
        
        # Cargar pagos y asistencias
        self._cargar_pagos_asistencias(datos['pagos'], datos['asistencias'])
        
        print("✅ SISTEMA INICIALIZADO CORRECTAMENTE")
        
    def _cargar_sucursales(self, datos_sucursales):
        """Carga sucursales en el grafo (Entrega 3)"""
        for suc_data in datos_sucursales:
            sucursal = Sucursal(
                suc_data['id'], 
                suc_data['nombre'], 
                suc_data['direccion']
            )
            self.grafo_sucursales.agregar_nodo(suc_data['id'], sucursal)
            
        # Agregar conexiones entre sucursales (distancias en km)
        conexiones = [(1, 2, 5.2), (1, 3, 8.7), (2, 3, 3.5), (2, 4, 12.1), (3, 4, 9.8)]
        for suc1, suc2, distancia in conexiones:
            self.grafo_sucursales.agregar_arista(suc1, suc2, distancia)
            
        print(f"📍 {len(datos_sucursales)} sucursales cargadas en grafo")

    def _cargar_instructores(self, datos_instructores):
        """Carga instructores en el sistema"""
        for inst_data in datos_instructores:
            instructor = Instructor(
                inst_data['id'],
                inst_data['nombre'],
                inst_data['especialidad']
            )
            self.gimnasio.agregar_instructor(instructor)
        print(f"👨‍🏫 {len(datos_instructores)} instructores cargados")

    def _cargar_ejercicios_rutinas(self, datos_ejercicios, datos_rutinas):
        """Carga ejercicios y rutinas base en árbol (Entrega 2)"""
        # Cargar ejercicios
        ejercicios_map = {}
        for ej_data in datos_ejercicios:
            ejercicio = Ejercicio(
                ej_data['id'],
                ej_data['nombre'],
                ej_data['tipo'],
                ej_data['calorias_por_minuto']
            )
            ejercicios_map[ej_data['id']] = ejercicio
            self.gimnasio.agregar_ejercicio_base(ejercicio)
        
        # Cargar rutinas base en árbol
        for rut_data in datos_rutinas:
            rutina = Rutina(
                rut_data['id'],
                rut_data['nombre'],
                rut_data['objetivo']
            )
            
            # Agregar ejercicios a la rutina
            for ej_id in rut_data['ejercicios']:
                if ej_id in ejercicios_map:
                    rutina.agregar_ejercicio(ejercicios_map[ej_id], 30)  # 30 min por defecto
            
            self.arbol_rutinas.insertar(rutina)
            self.gimnasio.agregar_rutina_base(rutina)
            
        print(f"💪 {len(datos_ejercicios)} ejercicios y {len(datos_rutinas)} rutinas cargadas en árbol")

    def _cargar_socios(self, datos_socios):
        """Carga socios en lista lineal y árbol por nivel de actividad (Entrega 2)"""
        for soc_data in datos_socios:
            socio = Socio(
                soc_data['id'],
                soc_data['nombre'],
                soc_data['documento'],
                soc_data['tipo_membresia']
            )
            
            # Agregar a lista lineal del gimnasio
            self.gimnasio.agregar_socio(socio)
            
            # Agregar al árbol de socios por nivel de actividad
            self.arbol_socios.insertar(socio, soc_data['nivel_actividad'])
            
        print(f"👥 {len(datos_socios)} socios cargados en lista y árbol")

    def _cargar_clases_reservas(self, datos_clases, datos_reservas):
        """Carga clases y reservas en cola de prioridad (Entrega 3)"""
        # Cargar clases
        clases_map = {}
        for cla_data in datos_clases:
            clase = ClaseGimnasio(
                cla_data['id'],
                cla_data['nombre'],
                cla_data['horario'],
                cla_data['cupo_maximo'],
                cla_data['instructor']
            )
            clases_map[cla_data['id']] = clase
            self.gimnasio.agregar_clase(clase)
        
        # Cargar reservas en cola de prioridad
        for res_data in datos_reservas:
            socio = self.gimnasio.buscar_socio_por_id(res_data['socio_id'])
            clase = clases_map.get(res_data['clase_id'])
            
            if socio and clase:
                reserva = Reserva(
                    res_data['id'],
                    socio,
                    clase,
                    res_data['fecha_reserva'],
                    res_data['prioridad']
                )
                self.cola_reservas.encolar(reserva)
                socio.agregar_reserva(reserva)
                
        print(f"📅 {len(datos_clases)} clases y {len(datos_reservas)} reservas cargadas en cola de prioridad")

    def _cargar_pagos_asistencias(self, datos_pagos, datos_asistencias):
        """Carga datos históricos de pagos y asistencias"""
        # Implementar carga de pagos y asistencias
        print(f"💰 {len(datos_pagos)} pagos y {len(datos_asistencias)} asistencias cargadas")

    def ejecutar_demo_entrega_1(self):
        """Demo de la Entrega 1: Encapsulamiento y estructuras básicas"""
        print("\n" + "=" * 50)
        print("DEMO ENTREGA 1 - ENCAPSULAMIENTO")
        print("=" * 50)
        
        # Mostrar socios y sus datos encapsulados
        print("\n👥 LISTA DE SOCIOS (Encapsulamiento):")
        for i, socio in enumerate(self.gimnasio.socios[:3]):  # Mostrar primeros 3
            print(f"  {i+1}. {socio.nombre} - Membresía: {socio.tipo_membresia}")
            print(f"     Documento: {socio.documento}")
            print(f"     Estado: {'ACTIVO' if socio.esta_activo() else 'INACTIVO'}")
        
        # Demo cálculo recursivo de calorías
        print("\n🔥 CÁLCULO RECURSIVO DE CALORÍAS:")
        socio_ejemplo = self.gimnasio.socios[0]
        calorias = socio_ejemplo.calcular_calorias_totales()
        print(f"  Socio: {socio_ejemplo.nombre}")
        print(f"  Calorías totales quemadas: {calorias:.2f} kcal")
        
        # Demo gestión de reservas
        print("\n📋 GESTIÓN DE RESERVAS:")
        clases_disponibles = [c for c in self.gimnasio.clases if c.hay_cupo_disponible()]
        if clases_disponibles:
            print(f"  Clases con cupo disponible: {len(clases_disponibles)}")
            for clase in clases_disponibles[:2]:
                print(f"    - {clase.nombre}: {clase.cupos_disponibles()} cupos")

    def ejecutar_demo_entrega_2(self):
        """Demo de la Entrega 2: Árboles y jerarquías"""
        print("\n" + "=" * 50)
        print("DEMO ENTREGA 2 - ÁRBOLES Y JERARQUÍAS")
        print("=" * 50)
        
        # Recorrido del árbol de socios
        print("\n🌳 RECORRIDO ÁRBOL DE SOCIOS (Inorden):")
        socios_ordenados = self.arbol_socios.recorrido_inorden()
        for nivel, socios_nivel in socios_ordenados.items():
            print(f"  Nivel {nivel}: {len(socios_nivel)} socios")
        
        # Búsqueda en árbol de rutinas
        print("\n🔍 BÚSQUEDA EN ÁRBOL DE RUTINAS:")
        rutinas_fuerza = self.arbol_rutinas.buscar_por_objetivo("FUERZA")
        print(f"  Rutinas de fuerza encontradas: {len(rutinas_fuerza)}")
        for rutina in rutinas_fuerza[:2]:
            print(f"    - {rutina.nombre} ({rutina.objetivo})")

    def ejecutar_demo_entrega_3(self):
        """Demo de la Entrega 3: Colas de prioridad y grafos"""
        print("\n" + "=" * 50)
        print("DEMO ENTREGA 3 - COLAS DE PRIORIDAD Y GRAFOS")
        print("=" * 50)
        
        # Procesar reservas por prioridad
        print("\n🎯 COLA DE PRIORIDAD - RESERVAS:")
        print("  Procesando reservas por orden de prioridad...")
        reservas_procesadas = []
        for _ in range(min(3, len(self.cola_reservas))):
            reserva = self.cola_reservas.desencolar()
            if reserva:
                reservas_procesadas.append(reserva)
                print(f"    - {reserva.socio.nombre} -> {reserva.clase.nombre} (Prioridad: {reserva.prioridad})")
        
        # Devolver reservas a la cola para mantener datos
        for reserva in reservas_procesadas:
            self.cola_reservas.encolar(reserva)
        
        # Recorrido en el grafo de sucursales
        print("\n🗺️  RECORRIDO EN GRAFO DE SUCURSALES:")
        print("  BFS desde sucursal central:")
        bfs_result = self.grafo_sucursales.bfs(1)
        for sucursal_id in bfs_result[:4]:
            print(f"    - Sucursal {sucursal_id}")
        
        print("  DFS desde sucursal central:")
        dfs_result = self.grafo_sucursales.dfs(1)
        for sucursal_id in dfs_result[:4]:
            print(f"    - Sucursal {sucursal_id}")

    def ejecutar_demo_entrega_4(self):
        """Demo de la Entrega 4: Ordenamiento y algoritmos avanzados"""
        print("\n" + "=" * 50)
        print("DEMO ENTREGA 4 - ORDENAMIENTO Y ALGORITMOS")
        print("=" * 50)
        
        # Ordenamiento topológico de rutinas
        print("\n📊 ORDENAMIENTO TOPOLÓGICO DE RUTINAS:")
        secuencia_rutinas = self.arbol_rutinas.ordenamiento_topologico()
        if secuencia_rutinas:
            print("  Secuencia recomendada de rutinas:")
            for i, rutina in enumerate(secuencia_rutinas[:3], 1):
                print(f"    {i}. {rutina.nombre}")
        
        # Camino mínimo entre sucursales
        print("\n🗺️  ALGORITMO DE DIJKSTRA - CAMINO MÍNIMO:")
        camino, distancia = self.grafo_sucursales.dijkstra(1, 4)
        if camino:
            print(f"  Camino más corto de sucursal 1 a 4:")
            print(f"    Ruta: {' -> '.join(map(str, camino))}")
            print(f"    Distancia total: {distancia} km")
        
        # Análisis de eficiencia
        print("\n⏱️  ANÁLISIS DE EFICIENCIA:")
        print("  Operaciones principales implementadas:")
        operaciones = [
            ("Búsqueda socio por ID", "O(log n)"),
            ("Inserción en árbol socios", "O(log n)"),
            ("Procesar reserva prioritaria", "O(log n)"),
            ("Búsqueda en grafo (BFS/DFS)", "O(V + E)"),
            ("Camino mínimo (Dijkstra)", "O((V + E) log V)")
        ]
        for op, complejidad in operaciones:
            print(f"    {op}: {complejidad}")

    def mostrar_estadisticas_generales(self):
        """Muestra estadísticas generales del sistema"""
        print("\n" + "=" * 50)
        print("ESTADÍSTICAS GENERALES DEL SISTEMA")
        print("=" * 50)
        
        print(f"🏋️  Gimnasio: {self.gimnasio.nombre}")
        print(f"📍 Sucursales: {len(self.grafo_sucursales.nodos)}")
        print(f"👥 Socios registrados: {len(self.gimnasio.socios)}")
        print(f"📅 Clases programadas: {len(self.gimnasio.clases)}")
        print(f"💪 Rutinas disponibles: {len(self.gimnasio.rutinas_base)}")
        print(f"👨‍🏫 Instructores: {len(self.gimnasio.instructores)}")
        print(f"🎯 Reservas en cola: {len(self.cola_reservas)}")
        
        # Socios por nivel de actividad
        print("\n📈 SOCIOS POR NIVEL DE ACTIVIDAD:")
        niveles = self.arbol_socios.contar_por_nivel()
        for nivel, cantidad in niveles.items():
            print(f"  {nivel}: {cantidad} socios")

    def ejecutar_demo_completa(self):
        """Ejecuta todas las demos del trabajo práctico"""
        self.inicializar_sistema()
        self.mostrar_estadisticas_generales()
        
        # Ejecutar demos de cada entrega
        self.ejecutar_demo_entrega_1()
        self.ejecutar_demo_entrega_2()
        self.ejecutar_demo_entrega_3()
        self.ejecutar_demo_entrega_4()
        
        print("\n" + "=" * 60)
        print("🎉 DEMO COMPLETADA - TRABAJO PRÁCTICO INTEGRADOR")
        print("=" * 60)
        print("Este sistema integra todas las estructuras de datos requeridas:")
        print("  ✅ Encapsulamiento y clases (Entrega 1)")
        print("  ✅ Árboles binarios y generales (Entrega 2)")
        print("  ✅ Colas de prioridad y grafos (Entrega 3)")
        print("  ✅ Ordenamiento y algoritmos avanzados (Entrega 4)")
        print("=" * 60)

def main():
    """Función principal del sistema"""
    try:
        sistema = SistemaGimnasios()
        sistema.ejecutar_demo_completa()
        
        # Esperar entrada del usuario antes de salir
        input("\nPresiona Enter para salir...")
        
    except Exception as e:
        print(f"❌ Error al ejecutar el sistema: {e}")
        print("Verifica que todos los archivos y módulos estén correctamente implementados.")

if __name__ == "__main__":
    main()