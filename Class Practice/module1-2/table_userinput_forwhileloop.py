# Table using for loop

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Table using while loop

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1
    