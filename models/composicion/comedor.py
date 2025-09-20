"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from typing import List

class Comedor:
    """
    Clase que implementa composición conteniendo una mesa y sillas.
    """

    def __init__(self, nombre: str, mesa: 'Mesa', sillas: List['Silla'] = None):
        """
        Constructor del comedor.
        """
        self._nombre = nombre
        self._mesa = mesa
        self._sillas = sillas if sillas is not None else []

    @property
    def nombre(self) -> str:
        """Getter para el nombre del comedor."""
        return self._nombre

    @property
    def mesa(self) -> 'Mesa':
        """Getter para la mesa del comedor."""
        return self._mesa

    @property
    def sillas(self) -> List['Silla']:
        """Getter para la lista de sillas."""
        return self._sillas.copy()  # Retorna una copia para proteger la lista interna

    def agregar_silla(self, silla: 'Silla') -> str:
        """
        Agrega una silla al comedor.
        """
        if not isinstance(silla, Silla):
            return "Error: Solo se pueden agregar objetos de tipo Silla"
        capacidad_maxima = self._calcular_capacidad_maxima()
        if len(self._sillas) >= capacidad_maxima:
            return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}"
        self._sillas.append(silla)
        return f"Silla {silla.nombre} agregada exitosamente al comedor"

    def quitar_silla(self, indice: int = -1) -> str:
        """
        Quita una silla del comedor.
        """
        if not self._sillas:
            return "No hay sillas para quitar"
        try:
            silla_removida = self._sillas.pop(indice)
            return f"Silla {silla_removida.nombre} removida del comedor"
        except IndexError:
            return "Índice de silla inválido"

    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total del comedor sumando todos sus componentes.
        """
        precio_total = self._mesa.calcular_precio()
        for silla in self._sillas:
            precio_total += silla.calcular_precio()
        # Aplicar descuento por set completo (5% si tiene 4 o más sillas)
        if len(self._sillas) >= 4:
            precio_total *= 0.95  # 5% de descuento
        return round(precio_total, 2)

    def obtener_descripcion_completa(self) -> str:
        """
        Obtiene una descripción completa del comedor y todos sus componentes.
        """
        descripcion = f"=== COMEDOR {self.nombre.upper()} ===\n\n"
        descripcion += "MESA:\n"
        descripcion += self._mesa.obtener_descripcion() + "\n\n"
        if self._sillas:
            descripcion += f"SILLAS ({len(self._sillas)} unidades):\n"
            for i, silla in enumerate(self._sillas, 1):
                descripcion += f"{i}. {silla.obtener_descripcion()}\n"
        else:
            descripcion += "SILLAS: Ninguna incluida\n"
        descripcion += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():.2f} ---"
        if len(self._sillas) >= 4:
            descripcion += "\n(Incluye 5% de descuento por set completo)"
        return descripcion

    def _calcular_capacidad_maxima(self) -> int:
        """
        Calcula la capacidad máxima de sillas basada en el tamaño de la mesa.
        Método privado auxiliar.
        """
        # Si la mesa tiene atributo 'capacidad_personas', úsalo
        if hasattr(self._mesa, 'capacidad_personas'):
            return self._mesa.capacidad_personas
        else:
            # Capacidad por defecto basada en el tamaño
            return 6  # Valor por defecto

    def obtener_resumen(self) -> dict:
        """
        Obtiene un resumen estadístico del comedor.
        """
        resumen = {
            "nombre": self.nombre,
            "total_muebles": 1 + len(self._sillas),  # mesa + sillas
            "precio_mesa": self._mesa.calcular_precio(),
            "precio_sillas": sum(silla.calcular_precio() for silla in self._sillas),
            "precio_total": self.calcular_precio_total(),
            "capacidad_personas": len(self._sillas),
            "materiales_utilizados": self._obtener_materiales_unicos()
        }
        return resumen

    def _obtener_materiales_unicos(self) -> list:
        """
        Obtiene una lista de materiales únicos usados en el comedor.
        Método privado auxiliar.
        """
        materiales = {self._mesa.material}
        for silla in self._sillas:
            materiales.add(silla.material)
            if hasattr(silla, 'material_tapizado') and silla.material_tapizado:
                materiales.add(silla.material_tapizado)
        return list(materiales)

    def __str__(self) -> str:
        """Representación en cadena del comedor."""
        return f"Comedor {self.nombre}: Mesa + {len(self._sillas)} sillas"

    def __len__(self) -> int:
        """Retorna el número total de muebles en el comedor."""
        return 1 + len(self._sillas)  # mesa + sillas