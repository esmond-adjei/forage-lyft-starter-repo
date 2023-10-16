from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self, current_mileage : int, last_service_mileage : int):
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    @property
    def current_mileage(self):
        return self._current_mileage
    
    @current_mileage.setter
    def current_mileage(self, value : int):
        self._current_mileage = value

    @property
    def last_service_mileage(self):
        return self._last_service_mileage
    
    @last_service_mileage.setter
    def last_service_mileage(self, value : int):
        self._last_service_mileage = value

    @abstractmethod
    def needs_service(self):
        pass
