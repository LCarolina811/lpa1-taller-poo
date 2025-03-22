from muebleria.mueble import Mueble

class Mesa(Mueble):
    def __init__(self, material, precio, longitud, ancho):
        super().__init__(material, precio)
        self.longitud = longitud
        self.ancho = ancho

    def calcular_precio_final(self):
        return round(self.precio * 1.15, 2)  # Ejemplo: 15% de impuesto

    def __str__(self):
        return f"{super().__str__()}, Longitud: {self.longitud}, Ancho: {self.ancho}"

