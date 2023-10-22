import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):

    def test_last_service_date(self):
        last_service_date = date(2010, 1, 1)
        battery = SpindlerBattery(date(2023, 1, 1), last_service_date)
        self.assertEqual(battery.last_service_date, last_service_date)

    def test_needs_service(self):
        last_service_date = date(2010, 1, 1)
        current_date = date(2023, 1, 1)
        some_date = date(2011, 1, 1)

        battery1 = SpindlerBattery(current_date, last_service_date)
        battery2 = SpindlerBattery(some_date, last_service_date)
        self.assertTrue(battery1.needs_service())
        self.assertFalse(battery2.needs_service())