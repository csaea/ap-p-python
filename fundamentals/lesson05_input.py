# USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---")

# Basic text input
name = input("Enter your name: ")
print("Hello,", name)

# Input is always stored as a string, even if you type a number
age = input("Enter your age: ")
print("You said your age is:", age, "(type:", type(age), ")")

# To use numbers, we must cast (convert) the string to int or float
age_number = int(age)
print("Next year, you will be:", age_number + 1)

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# ---------------------------------------------------------
# CHALLENGES
# ---------------------------------------------------------

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.
favorite_color = input("\nChallenge 1 - What is your favorite color? ")
print("Nice! I like", favorite_color, "too.")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.
num1 = float(input("\nChallenge 2 - Enter a number: "))
num2 = float(input("Enter another number: "))
sum_result = num1 + num2
print("The sum is:", sum_result)

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
import math
diameter = float(input("\nChallenge 3 - Enter the diameter of a circle: "))
radius = diameter / 2
circle_area = math.pi * (radius ** 2)
print("The area of the circle is:", circle_area)

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

sides = int(input("Enter how many sides the die should have: "))
die_roll = random.randint(1, sides)
print("You rolled a", die_roll, "on a", sides, "-sided die.")
