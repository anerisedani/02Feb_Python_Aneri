students = []

n = int(input("Enter number of students: "))

for i in range(n):
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    city = input("Enter City: ")

    student = {"id": id, "name": name, "city": city}
    students.append(student)

print(students)

