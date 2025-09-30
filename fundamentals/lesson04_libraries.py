#Key concepts: libraries in Python

#------------------
# MATH LIBRARY
#------------------
# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

print("\n--- Math Library ---\n")

print("Square root of 25: ", math.sqrt(25))
print("Ceiling of 4.2: ", math.ceil(4.2))
print("Floor of 4.8: ", math.floor(4.8))
print("Power (2^5): ", math.pow(2, 5))
print("Pi constant: ", math.pi)

#------------------
# RANDOM LIBRARY
#------------------

# Pseudorandom Nnumber Generators (PRNG) vs True random numbers (TRNG). 
# Watch Tom Scott video on lava lamps and randomness: https://www.youtube.com/watch?v=1cUUfMeOijg
# Optional video: Computerphile Random Numbers with LFSR (Linear Feedback Shift Register): https://www.youtube.com/watch?v=Ks1pw1X22y4

# Precurser challenge: Create your own pseudorandom number generator
# Start with a seed that is a float with at least 10 numbers total. 
# Perform a math calculation on it using addition, subtractions, and division. 
# Use math library to round the float up to an integer. 

import random
print("\n--- Random Library ---\n")

print("Random integer between 1 and 10: ", random.randint(1, 7))
print("Random float between 0 and 1: ", random.random())
print("Random choice from a list: ", random.choice(["red", "blue", "green"]))

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Givens: The formula to calculate a circle is πr² and a radius = diameter / 2
import math
radius = 14 / 2
circle_area = math.pi * (radius ** 2)
print("Circle Area:", circle_area)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.
import random
die_roll = random.randint(1, 6)
print("Die Roll:", die_roll)


