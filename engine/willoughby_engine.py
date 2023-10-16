from .engine import Engine


class WilloughbyEngine(Engine):

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
