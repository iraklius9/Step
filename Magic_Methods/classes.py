class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector dimensions are: ({self.x}, {self.y})"


# ========================================================================


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return f"The answer is: {self.title == other.title and self.author == other.author}"


# ========================================================================


class Car:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self):
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self):
        return f"{self._brand} {self._model} ({self._year})"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Year must be an integer")
        self._year = value
