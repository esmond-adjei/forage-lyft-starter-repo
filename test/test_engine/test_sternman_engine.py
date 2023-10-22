import unittest

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    
    def test_needs_service(self):
        last_service_mileage = 10000
        current_mileage = 20000
        some_mileage = 15000

        engine1 = SternmanEngine(warning_light_is_on=True, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        engine2 = SternmanEngine(warning_light_is_on=False, current_mileage=some_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine1.needs_service())
        self.assertFalse(engine2.needs_service())