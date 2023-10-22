from engine.engine import Engine


class CapuletEngine(Engine):
    __service_interval = 30000

    def needs_service(self) -> bool:
        return (self.current_mileage - self.last_service_mileage) > CapuletEngine.__service_interval
