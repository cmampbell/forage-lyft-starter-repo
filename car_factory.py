from abc import ABC, abstractmethod
from car import Car
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from battery import nubbin_battery
from battery import spindler_battery

class CarFactory(ABC):
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)

        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(current_date, last_service_date)

        return Car(engine, battery)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = sternman_engine(warning_light_on)
        battery = spindler_battery(current_date, last_service_date)

        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)

        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(current_date, last_service_date)

        return Car(engine, battery)
    