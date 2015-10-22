# Chapter 3
# mathLoop.py - Program that uses loops with a variable to perform
# various mathematic operations


xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Prints all numbers of list to a new line
for x in xs:
    print(x)

# Prints the square of all numbers in list
for y in xs:
    print(y ** 2)

# Stores the sum of all numbers in list to var
total = 0
for z in xs:
    total = total + z
print(total)

# Print the product of all numbers in list
square = 1 
for a in xs:
    square = square * a 
print(square)
