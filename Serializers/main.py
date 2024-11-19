from student_class import *

addresses = [
    Address('Tbilisi', 'Saburtalo'),
    Address('Tbilisi', 'Gldani-7-11-4-93'),
    Address('Tbilisi', 'Leselidzs str. 25'),
    Address('Tbilisi', 'Varketili IV 407-5-123')
]

students = [
    Student('Paata', 87, addresses[0]),
    Student('Teona', 92, addresses[1]),
    Student('Nino', 99, addresses[2]),
    Student('Andria', 87, addresses[3])
]

file_name = 'students.json'

save_students(students, file_name)

students_data = load_students(file_name)

students_data = update_student(students_data, row_id=1, new_mark=95)

with open(file_name, 'w') as file:
    json.dump(students_data, file, indent=2)
