from abc import abstractmethod
from models.mueble import Mueble

class Almacenamiento(Mueble):
    """
    Clase abstracta para muebles de almacenamiento.
    Hereda de Mueble y define atributos y métodos comunes.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float, capacidad: float, tipo_apertura: str):
        super().__init__(nombre, material, color, precio_base)
        self._capacidad = capacidad 
        self._tipo_apertura = tipo_apertura

    @property
    def capacidad(self) -> float:
        
        return self._capacidad

    @capacidad.setter
    def capacidad(self, value: float) -> None:
        if value < 0:
            raise ValueError("La capacidad no puede ser negativa")
        self._capacidad = value

    @property
    def tipo_apertura(self) -> str:

        return self._tipo_apertura

    @tipo_apertura.setter
    def tipo_apertura(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El tipo de apertura no puede estar vacío")
        self._tipo_apertura = value.strip()

    def obtener_descripcion(self) -> str:
        
        return (f"{self.nombre} de {self.material}, color {self.color}, "
                f"capacidad {self.capacidad}L, apertura tipo {self.tipo_apertura}")

    @abstractmethod
    def calcular_precio(self) -> float:
        
        pass