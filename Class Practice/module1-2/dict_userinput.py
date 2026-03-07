students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i+1)

    id = input("Enter ID: ")
    name = input("Enter Name: ")
    city = input("Enter City: ")

    students[id] = {"Name": name, "City": city}

print("\nStudent Data:")

for id, info in students.items():
    print("ID:", id)
    print("Name:", info["Name"])
    print("City:", info["City"])
    print()
