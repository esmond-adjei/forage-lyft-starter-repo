from engine.engine import Engine


class WilloughbyEngine(Engine):

    __service_interval = 60000

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > WilloughbyEngine.__service_interval
