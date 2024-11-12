from classes import *

# vector class
v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)

# book class
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)
print(book1 == book3)

# car class
car = Car('Toyota', 'Camry', 2020)
print(car)

car.brand = 'Mercedes'
print(car)
car.model = 'C-Class'
print(car)
car.year = 2021
print(car)



