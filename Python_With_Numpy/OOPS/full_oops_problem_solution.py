class Car:
    total_car = 0
    
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    def display(self):
       return f"{self.get_brand()} {self.__model}"
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol"
    @staticmethod
    def general_description():
        return "This is a general description of the car."
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity = battery_capacity
    def fuel_type(self):
        return "Electric"
    def display(self):
        return f"{self.get_brand()} {self.model} with battery capacity of {self.battery_capacity} kWh"

car1 = Car("Toyota", "Camry")
car3 = Car("Honda", "Civic")
print(car1.model)
car1.model = "Shah"
print(car1.model)
print(car1.general_description())
print("Total cars created:", Car.total_car)
print(car1.get_brand())
print(car1.model)
print(car1.display())
print(car1.fuel_type())

car2 = ElectricCar("Tesla", "Model S", 100)
print(isinstance(car2,Car))
print(isinstance(car2,ElectricCar))
print(car2.get_brand())
print(car2.model)
print(car2.battery_capacity)
print(car2.display())
print(car2.fuel_type())

class Battery:
    def battery_info(self):
        print("This is Battery")

class Engine:
    def engine_info(self):
        print("This is Engine")

class ElectricCarTwo(Battery,Engine):
    def electric_info():
        print("This is Electric Car Two")

electric = ElectricCarTwo()
print(electric.battery_info())
print(electric.engine_info())