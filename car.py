from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire):
        self._engine = engine
        self._battery = battery
        self._tire = tire

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self, value):
        self._battery = value

    @property
    def tire(self):
        return self._tire
    
    @tire.setter
    def tire(self, value):
        self._tire = value

    def needs_service(self):
        return self._engine.needs_service() or self._battery.needs_service() or self._tire.needs_service()
