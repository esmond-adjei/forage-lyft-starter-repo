from .engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on : bool, current_mileage=None, last_service_mileage=None):
        super().__init__(current_mileage, last_service_mileage)
        self._warning_light_is_on = warning_light_is_on

    @property
    def warning_light_is_on(self):
        return self._warning_light_is_on
    
    @warning_light_is_on.setter
    def warning_light_is_on(self, value : bool):
        self._warning_light_is_on = value

    def needs_service(self):
        return self.warning_light_is_on
