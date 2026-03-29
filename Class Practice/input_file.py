f1=open('data.txt','a')
n=int(input("enter number of students"))

for i in range(n):
   id=input("enter an id:")
   name=input("enter a name:")

   f1.write(f"id:{id}\n")
   f1.write(f"name:{name}\n")

