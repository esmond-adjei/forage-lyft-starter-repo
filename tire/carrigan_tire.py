from tire.tire import Tire


class CarriganTire(Tire):
    
    __service_threshold = 0.9

    def needs_service(self):
        for value in self.tire_wear_sensor_values:
            if value >= CarriganTire.__service_threshold:
                return True
        return False