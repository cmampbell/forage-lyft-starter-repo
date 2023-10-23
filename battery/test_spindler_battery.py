import unittest
from datetime import datetime, date

from spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_doesnt_need_service(self):
        last_service_date = datetime.today().date()

        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_does_need_service(self):
        last_service_date = date.fromisoformat("2020-10-23")

        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
