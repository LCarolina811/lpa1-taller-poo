from abc import ABC, abstractmethod
from models.mueble import Mueble

class Superficie(Mueble, ABC):
    """
    Clase abstracta para muebles de superficie.
    Hereda de Mueble y añade atributos específicos como área, forma y altura.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 area: float, forma: str, altura: float):
        super().__init__(nombre, material, color, precio_base)
        self._area = area  # en m2
        self._forma = forma  # ej: rectangular, circular
        self._altura = altura  # en cm

    @property
    def area(self) -> float:
        """Área de la superficie en metros cuadrados."""
        return self._area

    @area.setter
    def area(self, value: float) -> None:
        if value <= 0:
            raise ValueError("El área debe ser mayor a 0")
        self._area = value

    @property
    def forma(self) -> str:
        """Forma de la superficie."""
        return self._forma

    @forma.setter
    def forma(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("La forma no puede estar vacía")
        self._forma = value.strip()

    @property
    def altura(self) -> float:
        """Altura de la superficie en centímetros."""
        return self._altura

    @altura.setter
    def altura(self, value: float) -> None:
        if value <= 0:
            raise ValueError("La altura debe ser mayor a 0")
        self._altura = value

    def obtener_info_superficie(self) -> str:
        """
        Devuelve información específica de la superficie.
        Método concreto auxiliar para las clases hijas.
        """
        return (f"Área: {self.area} m², Forma: {self.forma}, Altura: {self.altura} cm")

    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Método abstracto para calcular el precio final.
        Debe ser implementado por las clases concretas.
        """
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Método abstracto para obtener la descripción completa.
        Debe ser implementado por las clases concretas.
        """
        pass