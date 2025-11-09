'''
GRAFO_SUCURSALES (Entrega 3)
    - nodos: dict[int, Sucursal]
    - aristas: dict[int, list[tuple[int, float]]]
    + agregar_conexion(sucursal1: int, sucursal2: int, distancia: float)
'''
from proyecto_gimnasio.sistema.sucursal import Sucursal
class GrafoSucursales:
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_sucursal(self, sucursal: Sucursal):
        self.nodos[sucursal.get_id_sucursal()] = sucursal
        self.aristas[sucursal.get_id_sucursal()] = []

    def agregar_conexion(self, sucursal1: int, sucursal2: int, distancia: float):
        if sucursal1 in self.nodos and sucursal2 in self.nodos:
            self.aristas[sucursal1].append((sucursal2, distancia))
            self.aristas[sucursal2].append((sucursal1, distancia))  # Asumiendo grafo no dirigido
        else:
            raise ValueError("Una o ambas sucursales no existen en el grafo.")  
    
    def obtener_conexiones(self, sucursal_id: int) -> list[tuple[int, float]]:
        return self.aristas.get(sucursal_id, [])
    
    def obtener_todas_sucursales(self) -> list[Sucursal]:
        return list(self.nodos.values())
    
    def contar_sucursales(self) -> int:
        return len(self.nodos)
    def contar_conexiones(self) -> int:
        total = 0
        for conexiones in self.aristas.values():
            total += len(conexiones)
        return total // 2  # Dividimos por 2 porque es un grafo no dirigido
    
    def obtener_sucursal(self, sucursal_id: int) -> Sucursal:
        return self.nodos.get(sucursal_id, None)
    
    def eliminar_sucursal(self, sucursal_id: int):
        if sucursal_id in self.nodos:
            del self.nodos[sucursal_id]
            del self.aristas[sucursal_id]
            for conexiones in self.aristas.values():
                conexiones[:] = [conn for conn in conexiones if conn[0] != sucursal_id]
        else:
            raise ValueError("La sucursal no existe en el grafo.")
    
    def eliminar_conexion(self, sucursal1: int, sucursal2: int):
        if sucursal1 in self.nodos and sucursal2 in self.nodos:
            self.aristas[sucursal1] = [conn for conn in self.aristas[sucursal1] if conn[0] != sucursal2]
            self.aristas[sucursal2] = [conn for conn in self.aristas[sucursal2] if conn[0] != sucursal1]
        else:
            raise ValueError("Una o ambas sucursales no existen en el grafo.")
        
    