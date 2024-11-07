from cars import Car, ElectricCar

car1 = Car("Toyota", "Prius", 2010)
car2 = Car("BMW", "X5", 2015)
car3 = Car("Mercedes", "S-Class", 2020)

print(car1.age_of_car())
print(car2.age_of_car())
print(car3.age_of_car())

electric_car1 = ElectricCar("Tesla", "Model S", 2022, 24)
electric_car2 = ElectricCar("Nissan", "Leaf", 2021, 20)

print(electric_car1.age_of_car())
print(electric_car2.age_of_car())

print(Car.total_cars())

car1.car_info()
electric_car1.car_info()
electric_car1.battery_info()
