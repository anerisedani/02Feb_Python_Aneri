#------------Banking System-------------

# Account opening function
def open_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current): ")
    
    balance = 0

    print("Account created successfully\n")

    return acc_no, name, acc_type, balance


# Deposit function
def deposit(balance):

    amount = int(input("Enter deposit amount: "))

    if amount >= 2000:
        balance = balance + amount
        print("Deposit successful")
    else:
        print("Minimum deposit is 2000")
    
    return balance


# Withdrawal function
def withdraw(balance):

    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
    else:
        print("Insufficient balance")

    return balance


# Statement function
def statement(acc_no, name, acc_type, balance):

    print("\n----- ACCOUNT STATEMENT -----")
    print("Account Number :", acc_no)
    print("Account Holder :", name)
    print("Account Type   :", acc_type)
    print("Balance        :", balance)

# Main program
acc_no = ""
name = ""
acc_type = ""
balance = 0

while True:

    print("\n----- BANK MENU -----")
    print("1. Account Opening")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no, name, acc_type, balance = open_account()

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        statement(acc_no, name, acc_type, balance)

    elif choice == "5":
        print("Thank you for using the Banking System!wish to see you soon:)")
        break

    else:
        print("Invalid choice")


