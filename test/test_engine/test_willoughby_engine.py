import unittest

from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    
    def test_needs_service(self):
        last_service_mileage = 10000
        current_mileage = 20000
        some_mileage = 15000

        engine1 = WilloughbyEngine(current_mileage, last_service_mileage)
        engine2 = WilloughbyEngine(some_mileage, last_service_mileage)
        self.assertTrue(engine1.needs_service())
        self.assertFalse(engine2.needs_service())