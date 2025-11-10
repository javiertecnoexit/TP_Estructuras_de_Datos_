'''
ARBOL_RUTINAS (Entrega 2)
    - raiz: NodoArbol
    + insertar_rutina(rutina: Rutina, padre: Rutina = None)
'''

from entidades.rutina import Rutina

class NodoArbolRutina:
    def __init__(self, rutina):
        self.rutina = rutina
        self.hijos = []
        
class ArbolRutinas:
    def __init__(self):
        self.raiz = None

    def insertar_rutina(self, rutina, padre=None):
        nuevo_nodo = NodoArbolRutina(rutina)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            nodo_padre = self._buscar_nodo(self.raiz, padre)
            if nodo_padre:
                nodo_padre.hijos.append(nuevo_nodo)

    def _buscar_nodo(self, nodo_actual, rutina_buscada):
        if nodo_actual.rutina == rutina_buscada:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self._buscar_nodo(hijo, rutina_buscada)
            if resultado:
                return resultado
        return None
    def obtener_todas_rutinas(self):
        rutinas = []
        self._obtener_todas_rutinas_recursivo(self.raiz, rutinas)
        return rutinas
    def _obtener_todas_rutinas_recursivo(self, nodo_actual, rutinas):
        if nodo_actual is not None:
            rutinas.append(nodo_actual.rutina)
            for hijo in nodo_actual.hijos:
                self._obtener_todas_rutinas_recursivo(hijo, rutinas)
    
    def contar_rutinas(self):
        return self._contar_rutinas_recursivo(self.raiz)
    def _contar_rutinas_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        contador = 1  # Contar el nodo actual
        for hijo in nodo_actual.hijos:
            contador += self._contar_rutinas_recursivo(hijo)
        return contador
    
    