print("Hello World!")
print('Hello World!')
print('''hello world!
      continues
      the broken line''')
#esacpe funtcion
print("hello \'python'!")
print('hello \"python"!')
print("hello \npython!")
print("\thello python!")
print("hel\blo \bpython!")

#end function
#seperate function
#comment function

#variable is a name which can store a value
#number=15
#cannot be started with a num or a special symbol

a=15
b=6
print("add:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)

#r is used for the raw string ; as it is statement would be the answer
#type method
#casting converts the data type into another data type

a=input("enter value of a =")
b=input("enter value of b=")
print("sum:",int(a)+int(b))

#input function
#split function

#format function
#operators
#1.assignment operator
#2.logical operator

sub1 = float(input("Enter marks of Subject 1 (out of 100): "))
sub2 = float(input("Enter marks of Subject 2 (out of 100): "))
sub3 = float(input("Enter marks of Subject 3 (out of 100): "))
sub4 = float(input("Enter marks of Subject 4 (out of 100): "))

# Calculate total
total = sub1 + sub2 + sub3 + sub4

# Calculate percentage
percentage = total / 4

# Decide grade
if percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

#print result
print("\n----- Marksheet -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)

if grade == "Fail":
    print("Result: You have Failed")
else:
    print("Result: You have Passed")