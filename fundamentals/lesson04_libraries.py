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
# Explain pseudorandom numbers. 
# Watch Tom Scott video on lava lamps and randomness: https://www.youtube.com/watch?v=1cUUfMeOijg
import random
print("\n--- Random Library ---")

print("Random integer between 1 and 10: ", random.randint(1, 10))
print("Random float between 0 and 1: ", random.random())
print("Random choice from a list: ", random.choice(["red", "blue", "green"]))

# Challenge 1: Circle Area
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# The formula to calculate a circle: πr² (Use math.pi for π) (radius = diameter / 2)

radius = 14 /2
circle_area = math.pi * (radius ** 2)
print("Circle Area:", circle_area)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

die_roll = random.randint(1, 6)
print("Die Roll:", die_roll)


