import unittest
from main import calcular_tarifa, formato_moneda, TARIFA_MOVIMIENTO, TARIFA_PARADO

class TestTaximetro(unittest.TestCase):

    def test_calculo_tarifa_movimiento(self):
        """Prueba que la tarifa en movimiento es correcta"""
        self.assertEqual(calcular_tarifa(10, True), 10 * TARIFA_MOVIMIENTO)

    def test_calculo_tarifa_parado(self):
        """Prueba que la tarifa cuando está detenido es correcta"""
        self.assertEqual(calcular_tarifa(5, False), 5 * TARIFA_PARADO)

    def test_formato_moneda_centimos(self):
        """Prueba que los valores menores a 1€ se muestran en céntimos"""
        self.assertEqual(formato_moneda(0.50), "50 céntimos")

    def test_formato_moneda_euros(self):
        """Prueba que los valores mayores o iguales a 1€ se muestran correctamente"""
        self.assertEqual(formato_moneda(1.25), "1.25€")


if __name__ == "__main__":
    unittest.main()
