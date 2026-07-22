# abstraction.py

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def mileage(self):
        pass


class Car(Vehicle):

    def mileage(self):
        print("Car Mileage: 20 km/l")


class Bike(Vehicle):

    def mileage(self):
        print("Bike Mileage: 65 km/l")


car = Car()
bike = Bike()

car.mileage()
bike.mileage()