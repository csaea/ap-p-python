# USER INPUT IN PYTHON

# Cool Tip: To comment one or more lines at a time: 
# highlight the lines, then click: ctrl + forward slash /

print("\n--- User Input ---\n")

# The value inside the input() command is a prompt to tell the user what to do. 
name = input("Enter your name:")

# Input defaults as a string, even if you type a number.
age = input("Enter your age: ")
print(type(age))

# use int() to convert a string to an integer
age_converted = int(age)
print("Next year, you will be:", age_converted + 1)
print(type(age_converted))

# Example with float input
height = float(input("Enter your height in meters:"))
print("You are", height, "meters tall.")

# CHALLENGES

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# Refer to lesson 3 or 4. 

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.