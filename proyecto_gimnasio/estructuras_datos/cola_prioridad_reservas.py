'''
COLA_PRIORIDAD_RESERVAS (Entrega 3)
    - heap: list[Reserva]
    + encolar(reserva: Reserva)
    + desencolar() -> Reserva

'''
from entidades.reserva import Reserva
import heapq    
class ColaPrioridadReservas:
    def __init__(self):
        self.heap = []

    def encolar(self, reserva: Reserva):
        # Usamos una tupla (prioridad, reserva) para que el heap se ordene por prioridad
        heapq.heappush(self.heap, (reserva.get_prioridad(), reserva))

    def desencolar(self) -> Reserva:
        if self.heap:
            return heapq.heappop(self.heap)[1]  # Devolvemos solo la reserva, no la prioridad
        else:
            return None
    def esta_vacia(self) -> bool:
        return len(self.heap) == 0
    
    def obtener_todas_reservas(self) -> list[Reserva]:
        return [item[1] for item in self.heap]  
    
    def contar_reservas(self) -> int:
        return len(self.heap)
    
    