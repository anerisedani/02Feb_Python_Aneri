class Student:

    def getdata(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print("Name:", self.name)
        print("ID:", self.id)


name = input("Enter name: ")
age = int(input("Enter ID: "))

s1 = Student(name, id)
s1.show()
