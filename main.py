from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

def main():
    silla = Silla("Madera", 100, 4)
    mesa = Mesa("Vidrio", 200, 150, 80)
    armario = Armario("Metal", 300, 2)

    print(silla)
    print(f"Precio final: ${silla.calcular_precio_final()}")

    print(mesa)
    print(f"Precio final: ${mesa.calcular_precio_final()}")

    print(armario)
    print(f"Precio final: ${armario.calcular_precio_final()}")

if __name__ == "__main__":
    main()
