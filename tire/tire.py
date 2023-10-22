from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, tire_wear_sensor_values: list):
        self._tire_wear_sensor_values = tire_wear_sensor_values
    
    @property
    def tire_wear_sensor_values(self):
        return self._tire_wear_sensor_values

    @tire_wear_sensor_values.setter
    def tire_wear_sensor_values(self, tire_wear_sensor_values):
        self._tire_wear_sensor_values = tire_wear_sensor_values
    
    @abstractmethod
    def needs_service(self):
        pass
