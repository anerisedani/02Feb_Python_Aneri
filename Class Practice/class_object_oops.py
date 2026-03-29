class Student:

    def get_data(self):
        self.name = input("Enter name: ")
        self.id = int(input("Enter id: "))

    def show_data(self):
        print("Name:", self.name)
        print("ID:", self.id)


# creating object
s1 = Student()

s1.get_data()
s1.show_data()
