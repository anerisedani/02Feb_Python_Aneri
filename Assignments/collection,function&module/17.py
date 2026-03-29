#Convert two lists into dictionary

keys = ["name", "age", "city"]
values = ["Aneri", 18, "Rajkot"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Dictionary:", my_dict)