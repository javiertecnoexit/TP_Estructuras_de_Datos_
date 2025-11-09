'''
PAGO
   ------------
   - id_pago: int
   - socio: Socio
   - monto: float
   - fecha_pago: datetime
   - tipo: str (MENSUALIDAD, CLASE_EXTRA, INSCRIPCION)
   - estado: str (PAGADO, PENDIENTE, VENCIDO)
'''
class Pago:
    def __init__(self, id_pago, socio, monto, fecha_pago, tipo, estado):
        self.__id_pago = id_pago
        self.__socio = socio
        self.__monto = monto
        self.__fecha_pago = fecha_pago
        self.__tipo = tipo
        self.__estado = estado

    ## Getters##############################################
    def get_id_pago(self):
        return self.__id_pago
    def get_socio(self):
        return self.__socio
    def get_monto(self):
        return self.__monto
    def get_fecha_pago(self):
        return self.__fecha_pago
    def get_tipo(self):
        return self.__tipo
    def get_estado(self):
        return self.__estado

    ## Setters##############################################
    def set_socio(self, socio):
        self.__socio = socio
    def set_monto(self, monto):
        self.__monto = monto
    def set_fecha_pago(self, fecha_pago):
        self.__fecha_pago = fecha_pago
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def set_estado(self, estado):
        self.__estado = estado
        