from muebleria.mueble import Mueble

class Silla(Mueble):
    def __init__(self, material, precio, num_patas):
        super().__init__(material, precio)
        self.num_patas = num_patas

    def calcular_precio_final(self):
        return round(self.precio * 1.1, 2)

    def __str__(self):
        return f"{super().__str__()}, Número de patas: {self.num_patas}"

