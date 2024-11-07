import csv
import os


def add_student():
    file_exists = os.path.exists('students.csv')
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['id', 'name', 'age', 'grade', 'subject_name', 'mark'])

    while True:
        id = input("Enter id: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")
        subject_name = input("Enter subject name: ")
        mark = input("Enter mark: ")

        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, age, grade, subject_name, mark])

        continue_ = input("Do you want to add another student? (y/n): ")
        if continue_.lower() != 'y':
            break

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        sorted_list = sorted(
            (row for row in reader if row and len(row) == 6),
            key=lambda row: int(row[0])
        )

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(sorted_list)


def read_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<5} {row[3]:<7} {row[4]:<15} {row[5]:<5}")


def average_mark():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        marks = []
        for row in reader:
            marks.append(int(row[5]))

        if marks:
            average = sum(marks) / len(marks)
            print(f"Average mark: {average}")
        else:
            print("No marks available")


def update_mark():
    id = input("Enter id: ")
    subject_name = input("Enter subject: ")
    new_mark = input("Enter new mark: ")

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = [row for row in reader]

    for row in rows:
        if row[0] == id and row[4] == subject_name:
            row[5] = new_mark

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


add_student()
read_students()
average_mark()
update_mark()
