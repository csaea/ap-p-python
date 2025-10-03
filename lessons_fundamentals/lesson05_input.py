# USER INPUT IN PYTHON

# print("\n--- User Input Demonstration ---")

# ctrl + forward slash /
name = input("Enter your name: ")

age = int(input("Enter your age: "))
age = input("Enter your age: ")
print(type(age))

age_number = int(age)
print("Next year, you will be:", age_number + 1)
print(type(age_number))

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

numberone = int(input("Pick any number: "))
numbertwo = int(input("Pick another number: "))
print(numberone + numbertwo)


# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# Refer to lesson 3 or 4. 

import math
diamter = int(input("Gimme a number "))
radius = diamter / 2
area = math.pi * radius ** 2
print("The area is ", area)

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random
sides = int(input("Give me a number of sides: "))
roll = random.randint(1, sides)
print("You rolled", roll)