from abc import ABC, abstractmethod
from car import Car

class Servicable(Car, ABC):

    @abstractmethod
    def needs_service(self):
        pass