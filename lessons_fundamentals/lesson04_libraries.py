# Python libraries are collections of pre-written code that you can import and use in your own programs.
# Doc on libraries: https://docs.python.org/3/library/index.html

#Key concepts: libraries, import math, import random

#------------------
# MATH LIBRARY
#------------------

# Doc on Math library: https://docs.python.org/3/library/math.html

import math
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up to an integer: ", math.ceil(4.2))
print("Round down to an integer: ", math.floor(4.8))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)


#------------------
# RANDOM LIBRARY
#------------------

# Pseudorandom Nnumber Generators (PRNG) vs True random numbers (TRNG). 
# Watch Tom Scott video on lava lamps and randomness: https://www.youtube.com/watch?v=1cUUfMeOijg
# Optional video: Computerphile Random Numbers with LFSR (Linear Feedback Shift Register): https://www.youtube.com/watch?v=Ks1pw1X22y4

# ** PRECURSER CHALLENGE **
# Create your own Pseudorandom Number Generator (PRNG) that utilizes a seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float DOWN to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

##### 
# 
print("------\n\n")
import math 

seed = 12.4444
step1 = seed / 6.7
step2 = step1 - 800
step3 = step2 + 180843
step4 = step3 % 10
result = math.floor(step4) + 1
print(result)

# limitednumber = step3 - result
# answer = math.floor(limitednumber * 10)


print("\n--- Random Library ---\n")

import random

# methods:
print("Random integer: ", random.randint(1, 7))
print("Random float between 0 and 1: ", random.random())
my_favs = ["taco", "burrito", "enchilada", "quesadilla"]
print(random.choice(my_favs))
random.shuffle(my_favs)
print(my_favs)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.