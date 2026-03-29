'''end: 
This assignment demonstrates the basic concepts of:
Lists
Tuples
Dictionary
Functions
Lambda
Modules (math & random)'''

'''Theory (Heading Wise)
1. List (Introduction)
A list in Python is a collection of elements that can store multiple values in a single 
variable. Lists are ordered, changeable (mutable), and allow duplicate values. Elements in a 
list can be of different data types such as integer, float, string, and boolean.

2. Length of List
The length of a list means the total number of elements present in the list. Python provides 
the built-in function len() to calculate the number of items in a list.

3. Updating a List (insert() and append())
Lists can be modified after creation:
insert(index, value) → Adds an element at a specific position.
append(value) → Adds an element at the end of the list.
This shows that lists are mutable (changeable).

4. Removing Elements from List
Elements can be removed using:
pop() → Removes the last element or element at a specific index.
remove(value) → Removes a specific element by its value.
These methods help in modifying list contents dynamically.

5. Iterating Through a List
Iteration means accessing each element one by one. In Python, we use a for loop to iterate 
through a list. This is useful for processing or displaying all elements.

6. Adding Elements Using Loop
An empty list can be filled using a for loop and append(). This is useful when elements are 
generated dynamically or based on conditions.

7. List to Tuple Conversion
A tuple is similar to a list but immutable (cannot be changed). A list can be converted into 
a tuple using the tuple() function.

8. Tuple with Multiple Data Types
A tuple can store elements of different data types like integers, strings, floats, and boolean
 values. Tuples are ordered but unchangeable.

9. Concatenation of Tuples
Two or more tuples can be combined using the + operator. This creates a new tuple containing
 elements of both tuples.

10. Accessing Tuple Elements (Indexing)
Tuple elements can be accessed using index numbers, starting from 0. The first element is at
 index 0.

11. Slicing in Tuple
Slicing allows accessing a range of elements using start and end index. It follows the format:
tuple[start:end]

12. Accessing Last Element in Tuple
The last element of a tuple can be accessed using negative indexing:
-1 refers to the last element.

13. Dictionary (Introduction)
A dictionary is a collection of key-value pairs. It is:
Unordered
Changeable (mutable)
Does not allow duplicate keys
Each key is unique and is used to access its corresponding value.

14. Accessing Dictionary Values
Values in a dictionary are accessed using their keys instead of index numbers.

15. Updating Dictionary Values
Dictionary values can be updated by assigning a new value to an existing key. This shows
 dictionaries are mutable.

16. keys() and values() Methods
keys() → Returns all keys in the dictionary
values() → Returns all values in the dictionary
These methods help in separating and viewing data.

17. Creating Dictionary from Two Lists
Two lists (one for keys and one for values) can be combined to form a dictionary using a
 loop. Each element from the key list is mapped to the corresponding value.

18. Character Frequency in String
A string can be analyzed to count how many times each character appears. This is done using
 a dictionary where:
Character = Key
Count = Value

19. Functions in Python
A function is a block of code that performs a specific task. It helps in:
Code reusability
Better organization
Functions are defined using the def keyword.

20. Parameterized Function
A function that accepts inputs (arguments) is called a parameterized function. These inputs
 are used inside the function to perform operations.

21. Lambda Function (Single Expression)
A lambda function is a small anonymous function written in one line. It contains only one 
expression and does not require a name.

22. Lambda Function (Multiple Arguments)
Lambda functions can take multiple inputs (arguments) but still contain only one expression.
 They are useful for short operations.

23. Math Module
Python provides a built-in math module that includes mathematical functions such as:
Square root
Power
Factorial
It must be imported using import math.

24. Random Module
The random module is used to generate random numbers.
Function:
randint(a, b) → Generates a random number between a and b.'''