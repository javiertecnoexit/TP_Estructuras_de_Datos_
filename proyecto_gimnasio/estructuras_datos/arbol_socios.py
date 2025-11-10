'''
ARBOL_SOCIOS (Entrega 2)
    - raiz: NodoArbol
    + insertar_socio(socio: Socio)
    + buscar_por_nivel_actividad(nivel: str) -> list[Socio]
'''
from entidades.socio import Socio
class NodoArbol:
    def __init__(self, socio):
        self.socio = socio
        self.izquierda = None
        self.derecha = None
class ArbolSocios:
    def __init__(self):
        self.raiz = None

    def insertar_socio(self, socio):
        nuevo_nodo = NodoArbol(socio)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.socio.get_id_socio() < nodo_actual.socio.get_id_socio():
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)

    def buscar_por_nivel_actividad(self, nivel):
        resultados = []
        self._buscar_por_nivel_recursivo(self.raiz, nivel, resultados)
        return resultados

    def _buscar_por_nivel_recursivo(self, nodo_actual, nivel, resultados):
        if nodo_actual is not None:
            if nodo_actual.socio.get_nivel_actividad() == nivel:
                resultados.append(nodo_actual.socio)
            self._buscar_por_nivel_recursivo(nodo_actual.izquierda, nivel, resultados)
            self._buscar_por_nivel_recursivo(nodo_actual.derecha, nivel, resultados)
    
    def obtener_todos_socios(self):
        socios = []
        self._obtener_todos_socios_recursivo(self.raiz, socios)
        return socios
    def _obtener_todos_socios_recursivo(self, nodo_actual, socios):
        if nodo_actual is not None:
            socios.append(nodo_actual.socio)
            self._obtener_todos_socios_recursivo(nodo_actual.izquierda, socios)
            self._obtener_todos_socios_recursivo(nodo_actual.derecha, socios)
    
    def contar_socios(self):
        return self._contar_socios_recursivo(self.raiz)
    def _contar_socios_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._contar_socios_recursivo(nodo_actual.izquierda) + self._contar_socios_recursivo(nodo_actual.derecha)    
    