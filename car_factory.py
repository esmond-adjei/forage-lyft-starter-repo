from datetime import date

from car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoPrimeTire


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Calliope:	Capulet Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Glissade:	Willoughby Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tire = OctoPrimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list) -> Car:
        # Palindrome: Sternman Engine	Spindler Battery
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        tire = OctoPrimeTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Rorschach: Willoughby Engine	Nubbin Battery
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        tire = CarriganTire(tire_wear)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        # Thovex: Capulet Engine	Nubbin Battery
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire = OctoPrimeTire(tire_wear)
        return Car(engine, battery, tire)


if __name__ == '__main__':
    from datetime import date
    from car_factory import CarFactory

    current_date = date(2023, 1, 1)
    last_service_date = date(2022, 1, 1)
    current_mileage = 10000
    last_service_mileage = 5000
    tire_wear = [0.1, 0.2, 0.3, 0.4, 0.5]

    calliope = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
    print(calliope.needs_service())

    glissade = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
    print(glissade.needs_service())

    palindrome = CarFactory.create_palindrome(current_date, last_service_date, True, tire_wear)
    print(palindrome.needs_service())

    rorschach = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
    print(rorschach.needs_service())

    thovex = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
    print(thovex.needs_service())