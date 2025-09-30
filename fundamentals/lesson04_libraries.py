#Key concepts: libraries in Python

#------------------
# MATH LIBRARY
#------------------
# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up: ", math.ceil(4.2))
print("Round down: ", math.floor(4.8))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)

#------------------
# RANDOM LIBRARY
#------------------

# Pseudorandom Nnumber Generators (PRNG) vs True random numbers (TRNG). 
# Watch Tom Scott video on lava lamps and randomness: https://www.youtube.com/watch?v=1cUUfMeOijg
# Optional video: Computerphile Random Numbers with LFSR (Linear Feedback Shift Register): https://www.youtube.com/watch?v=Ks1pw1X22y4

# ** PRECURSER CHALLENGE **
# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform math calculations on it using addition, subtraction, and division. 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

import random
print("\n--- Random Library ---\n")

print("Random integer: ", random.randint(1, 7))
print("Random float between 0 and 1: ", random.random())
print("Random choice from list: ", random.choice(["taco", "burrito", "enchilada", "quesadilla"]))

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2
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
print("You rolled a:", die_roll)


