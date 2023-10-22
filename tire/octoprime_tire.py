from tire.tire import Tire


class OctoPrimeTire(Tire):

    __service_threshold = 3

    def needs_service(self):
        return sum(self.tire_wear_sensor_values) >= OctoPrimeTire.__service_threshold
