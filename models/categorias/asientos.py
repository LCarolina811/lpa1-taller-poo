from abc import ABC, abstractmethod
from models.mueble import Mueble

class Asiento(Mueble, ABC):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, material de tapizado, etc.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        super().__init__(nombre, material, color, precio_base)
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado

    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        if value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value

    @property
    def tiene_respaldo(self) -> bool:
        """Getter para si tiene respaldo."""
        return self._tiene_respaldo

    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        self._tiene_respaldo = bool(value)

    @property
    def material_tapizado(self) -> str:
        """Getter para el material de tapizado."""
        return self._material_tapizado

    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        if value is not None and not value.strip():
            raise ValueError("El material de tapizado no puede estar vacío si se especifica")
        self._material_tapizado = value.strip() if value else None

    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.
        """
        factor = 1.0
        if self.tiene_respaldo:
            factor += 0.1
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1
        if self.capacidad_personas > 1:
            factor += 0.05 * (self.capacidad_personas - 1)
        return factor

    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.
        """
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info

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