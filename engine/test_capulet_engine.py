import unittest

from capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_doesnt_need_service(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_does_need_service(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
