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