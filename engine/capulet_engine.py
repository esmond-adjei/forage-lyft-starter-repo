from .engine import Engine


class CapuletEngine(Engine):

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
