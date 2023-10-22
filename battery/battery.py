from datetime import date
from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, current_date: date, last_service_date: date):
        self._current_date = current_date
        self._last_service_date = last_service_date

    @property
    def current_date(self) -> date:
        return self._current_date
    
    @current_date.setter
    def current_date(self, value: date):
        self._current_date = value

    @property
    def last_service_date(self) -> date:
        return self._last_service_date
    
    @last_service_date.setter
    def last_service_date(self, value: date):
        self._last_service_date = value

    @abstractmethod
    def needs_service(self):
        pass
