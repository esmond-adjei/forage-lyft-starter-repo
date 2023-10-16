from .battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        years_since_service = (self.current_date.year - self.last_service_date.year)
        return years_since_service >= 2