from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

    def __str__(self):
        return f"Material: {self.material}, Precio: ${self.precio}"

