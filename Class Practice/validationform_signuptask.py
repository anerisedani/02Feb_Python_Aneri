# signup_validation.py

import re   # module for regular expressions


# ----------- FUNCTIONS -----------

# 1. First Name & Last Name Validation
def validate_name(name):
    pattern = "^[A-Za-z]{2,}$"   # only letters, minimum 2 characters
    if re.match(pattern, name):
        return True
    else:
        return False


# 2. Email Validation
def validate_email(email):
    pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False


# 3. Password Validation
def validate_password(password):
    pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{6,}$"
    # Must contain:
    # 1 uppercase, 1 lowercase, 1 digit, 1 special character, min length 6
    if re.match(pattern, password):
        return True
    else:
        return False


# 4. Confirm Password
def confirm_password(password, confirm):
    return password == confirm


# 5. Mobile Number Validation
def validate_mobile(mobile):
    pattern = "^[0-9]{10}$"   # exactly 10 digits
    if re.match(pattern, mobile):
        return True
    else:
        return False


# ----------- MAIN PROGRAM -----------

print("----- SIGN UP FORM -----")

fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
confirm = input("Confirm Password: ")
mobile = input("Enter Mobile Number: ")


# ----------- VALIDATION -----------

if not validate_name(fname):
    print("Invalid First Name")

elif not validate_name(lname):
    print("Invalid Last Name")

elif not validate_email(email):
    print("Invalid Email")

elif not validate_password(password):
    print("Weak Password")

elif not confirm_password(password, confirm):
    print("Passwords do not match")

elif not validate_mobile(mobile):
    print("Invalid Mobile Number")

else:
    print("Signup Successful ✅")