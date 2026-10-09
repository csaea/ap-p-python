# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(4.8)
print(f"Round down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANTS are variables that NEVER change. They are written in ALL CAPS
PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator 

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# 1. The seed should be a INTEGER with five total digits. 
# 2. Perform oneat least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# Test if it works by changing your SEED integer value (on the left side of the decimal point)
# BONUS CHALLENGE: Make your random number always output below 10. 

# Simple version:
seed = 7265

calcs = seed + 2234 * 22 / 3
print(calcs)
randint = math.ceil(calcs)

print(f"Simple random num gen: {randint % 10}")
# Change the seed, get a new, pseudorandom number

for s in range(5):

    step1 = seed / 6.7
    # print(step1)
    step2 = step1 - 800.33
    # print(step2)
    step3 = step2 ** 3 
    # print(step3)
    round_up = math.ceil(step3)  
    result = round_up % 10 # remainder between 0 and 6 (never 6)
    print("Your random num is:", result)

    seed = seed * 3 