class Bank:

    def get_data(self):
        self.acc_no = input("Enter Account Number: ")
        self.name = input("Enter Name: ")
        self.balance = int(input("Enter Balance: "))

    def deposit(self):
        amount = int(input("Enter deposit amount: "))

        if amount >= 2000:
            self.balance = self.balance + amount
            print("Deposit done")
        else:
            print("Minimum deposit is 2000")

    def withdraw(self):
        amount = int(input("Enter withdraw amount: "))
        self.balance = self.balance - amount
        print("Withdrawal done")

    def show_data(self):
        print("\n--- ACCOUNT DETAILS ---")
        print("Account No:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)

b1 = Bank()
b1.get_data()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Details")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        b1.deposit()

    elif choice == "2":
        b1.withdraw()

    elif choice == "3":
        b1.show_data()

    elif choice == "4":
        break 