from battery.battery import Battery


class NubbinBattery(Battery):
    __service_duration = 4

    def needs_service(self) -> bool:
        years_since_service = (self.current_date.year - self.last_service_date.year) # 2023 - 2010 = 13
        return years_since_service > NubbinBattery.__service_duration # 13 > 4 = True
