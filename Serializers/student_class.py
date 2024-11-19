import json


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def to_dict(self):
        return {"city": self.city, "street": self.street}


class Student:
    id_counter = 1

    def __init__(self, name, mark, address):
        self.name = name
        self.mark = mark
        self.address = address
        self.row_id = Student.id_counter
        self.grade = self.calculate_grade()
        Student.id_counter += 1

    def calculate_grade(self):
        if self.mark >= 91:
            return 'A'
        elif self.mark >= 81:
            return 'B'
        elif self.mark >= 71:
            return 'C'
        else:
            return 'D'

    def to_dict(self):
        return {
            "row_id": self.row_id,
            "name": self.name,
            "mark": self.mark,
            "address": self.address.to_dict(),
            "grade": self.grade
        }


def save_students(students, filename):
    with open(filename, 'w') as file:
        json.dump([student.to_dict() for student in students], file, indent=2)


def load_students(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def update_student(data, row_id, new_mark):
    for student in data:
        if student["row_id"] == row_id:
            student["mark"] = new_mark
            student["grade"] = (
                'A' if new_mark >= 91 else
                'B' if new_mark >= 81 else
                'C' if new_mark >= 71 else
                'D'
            )
            break
    return data
