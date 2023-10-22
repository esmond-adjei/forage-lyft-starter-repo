from datetime import date

from car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Calliope:	Capulet Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Glissade:	Willoughby Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        # Palindrome: Sternman Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Rorschach: Willoughby Engine	Nubbin Battery
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        # Thovex: Capulet Engine	Nubbin Battery
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)


if __name__ == '__main__':
    from datetime import date
    from car_factory import CarFactory

    current_date = date(2023, 1, 1)
    last_service_date = date(2022, 1, 1)
    current_mileage = 10000
    last_service_mileage = 5000

    calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    print(calliope.needs_service())

    glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    print(glissade.needs_service())

    palindrome = CarFactory.create_palindrome(current_date, last_service_date, True)
    print(palindrome.needs_service())

    rorschach = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    print(rorschach.needs_service())

    thovex = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
    print(thovex.needs_service())