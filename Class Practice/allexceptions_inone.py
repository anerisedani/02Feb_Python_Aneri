"""try:
    # risky code
except:
    # error handling
else:
    # runs if no error
finally:
    # always runs"""

try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    result = a / b

except:
    print("Error occurred")

else:
    print("Result is:", result)

finally:
    print("Program ended")

#all exceptions in one are depicted here 