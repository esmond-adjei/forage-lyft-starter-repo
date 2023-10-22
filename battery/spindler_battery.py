from battery.battery import Battery


class SpindlerBattery(Battery):
    __service_duration = 2

    def needs_service(self) -> bool:
        years_since_service = (self.current_date.year - self.last_service_date.year)
        print(years_since_service)
        return years_since_service > SpindlerBattery.__service_duration