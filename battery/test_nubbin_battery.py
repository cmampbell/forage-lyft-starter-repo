import unittest
from datetime import datetime, date

from nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_doesnt_need_service(self):
        last_service_date = datetime.today().date()

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_does_need_service(self):
        last_service_date = date.fromisoformat("2018-10-23")

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
