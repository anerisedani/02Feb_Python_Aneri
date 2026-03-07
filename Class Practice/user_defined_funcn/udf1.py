# function to get and print student data
def student_data():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    print("Student ID:", id)
    print("Student Name:", name)


# function to add two numbers
def addition():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 + num2

    print("Addition is:", sum)

# calling the functions
student_data()
addition()
