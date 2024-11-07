import datetime


class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def age_of_car(self):
        current_year = datetime.datetime.now().year
        return f"{self.model}_ის ასაკია: {current_year - self.year}"

    @staticmethod
    def total_cars():
        return f"მანქანების სრული რაოდენობაა: {Car.number_of_cars}"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"{self.model}_ის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")
