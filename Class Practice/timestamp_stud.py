from datetime import datetime
import random

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    city = input("Enter City: ")

    student = {
        "id": random.randint(1000, 9999),
        "name": name,
        "city": city,
        "time": datetime.now()
    }

    students.append(student)

print(students)

