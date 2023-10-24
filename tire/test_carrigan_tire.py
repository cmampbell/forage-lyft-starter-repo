import unittest
from datetime import datetime, date

from carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_doesnt_need_service(self):
        tire_array = [0,0,0,0]

        tire = CarriganTire(tire_array)
        self.assertFalse(tire.needs_service())

    def test_does_need_service(self):
        tire_array = [.56, .45, .92, .87]

        tire = CarriganTire(tire_array)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()