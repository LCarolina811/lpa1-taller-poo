from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario

def test_silla():
    silla = Silla("Madera", 100, 4)
    assert silla.material == "Madera"
    assert silla.precio == 100
    assert silla.num_patas == 4
    assert silla.calcular_precio_final() == 110.00

def test_mesa():
    mesa = Mesa("Vidrio", 200, 150, 80)
    assert mesa.material == "Vidrio"
    assert mesa.precio == 200
    assert mesa.longitud == 150
    assert mesa.ancho == 80
    assert mesa.calcular_precio_final() == 230.00

def test_armario():
    armario = Armario("Metal", 300, 2)
    assert armario.material == "Metal"
    assert armario.precio == 300
    assert armario.num_puertas == 2
    assert armario.calcular_precio_final() == 360.00
