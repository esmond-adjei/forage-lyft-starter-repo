import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):

    def test_needs_service(self):
        tire_wear_sensor_values = [0.1, 0.2, 0.3, 0.4, 0.5]
        tire = CarriganTire(tire_wear_sensor_values)
        
        self.assertTrue(tire.needs_service())

        new_tire_wear_sensor_values = [0.2, 0.3, 0.4, 0.8, 1.6]
        tire.tire_wear_sensor_values = new_tire_wear_sensor_values
        
        self.assertFalse(tire.needs_service())
