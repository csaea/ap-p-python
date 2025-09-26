#Key concepts: libraries in Python

# MATH LIBRARY

import math

print("\n--- Math Library ---")

print("Square root of 25: ", math.sqrt(25))
print("Ceiling of 4.2: ", math.ceil(4.2))
print("Floor of 4.8: ", math.floor(4.8))
print("Power (2^5): ", math.pow(2, 5))
print("Pi constant: ", math.pi)

# RANDOM LIBRARY

import random
print("\n--- Random Library ---")

print("Random integer between 1 and 10: ", random.randint(1, 10))
print("Random float between 0 and 1: ", random.random())
print("Random choice from a list: ", random.choice(["red", "blue", "green"]))

# Challenge 1: Physics Problem (Kinetic Energy)

# Challenge 2: Circle Area
# Use the formula πr² to calculate the area of a circle with a diameter of 14. (Use math.pi for π.)
# Include an expression that calculates the radius based on its diameter (Diameter = r2)
circle_area = math.pi * (7 ** 2)
print("Challenge 2 - Circle Area:", circle_area)
