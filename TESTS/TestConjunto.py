import unittest
from src.logica.Conjunto import Conjunto
class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([2,4,7])
        self.assertIsNone(conjunto.promedio())