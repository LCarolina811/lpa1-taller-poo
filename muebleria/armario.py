from muebleria.mueble import Mueble

class Armario(Mueble):
    def __init__(self, material, precio, num_puertas):
        super().__init__(material, precio)
        self.num_puertas = num_puertas

    def calcular_precio_final(self):
        return round(self.precio * 1.2, 2)  # Ejemplo: 20% de impuesto

    def __str__(self):
        return f"{super().__str__()}, Número de puertas: {self.num_puertas}"

