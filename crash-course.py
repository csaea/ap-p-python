import math

# comment
# Python ignores anything after a #. Use comments to explain your code.

# to comment multiple lines,
# highlight the lines,
# and click ctrl + / 

print("Hello world!")   # print() displays output in the console

# VARIABLE DECLARATIONS AND DATA TYPES:
# A variable stores a value. Python figures out the data type for you.

a = 4           # integer 
b = 5.5         # float 
c = "CSAEA"     # string
d = False       # boolean 

print(a)
print(a, b, c, d)

# MATH OPERATORS 
# + - / *    %  **  //
# +=   -=   /=   
# % gives the remainder, ** is an exponent, // divides and drops the decimal
# e += 20 is shorthand for e = e + 20

e = 3 - 1
print(e)
e += 20
print(e)

# f-string, formatted strings
# Put f before the quotes. Anything inside { } is replaced with its value.

print(f"e is equal to {e}")

e -= 7 
e += 12

print(f"e is NOW equal to {e}")

# COMPARISONS (booleans, which always return True or False)

#  <   >    <=   >=    ==    !=
# == checks if two values are equal. A single = assigns a value.

print(5 <=  5)
print(7 == 4)
print(1 != 2)

isEqual = "Yes" != "YES"   # strings are case-sensitive
print(isEqual)

# LOGICAL OPERATORS
# In order of precedence: not   and   or
# not flips a boolean, and needs BOTH sides True, or needs AT LEAST ONE True

f = False
t = True

#predict output before running code. 
print(not f) # True
print( f and t) #False
print(f or t) #True
print(f or t and not f) # True

# CASTING ()
# Casting converts a value from one data type to another.

g = int(5.6536539) # changes float to int
h = str(54) # changes int 54 to string "54"
print(g) # changes data type to int and chops off (truncates) everything after decimal

# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2+ s3 # concatenate with +
end += ", Cowboy."

print(end + "\n")   # \n adds a new line

# MATH LIBRARY (import math at the top of the document)
# ceil rounds up, floor rounds down, pow always returns a float

print(math.sqrt(14))
print(math.ceil(3.65)) # rounds up to 4.0
print(math.floor(8.94)) # rounds down to 8.0
print(math.pow(2, 4))

# CONDITIONALS

# if    elif    else 
# Python checks top to bottom and runs only the FIRST block that is True.
# The indented lines belong to the condition above them.

t = True
f = False

if f: 
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else: 
    print("Reached else")


if 2 > 1 and 1 == 1: 
    print("Reached the first condition")
elif 6 == 7 or 3 != 3:
    print("Reached second condition")
elif 10 != 10:
    print("Reached third condition")
else: 
    print("Reached else")

# LISTS
# A list can hold any type, and can grow or shrink at any time.
# Indexes start at 0. Negative indexes count back from the end (-1 is the last item).

#index: 0   1   2   3   4
nums = [34, 52, 3, 64, 32]

print(nums)
print(nums[3]) #predict
print(nums[0])
print(nums[-1])
print(nums[-3])
print(nums[0] + nums[2])

nums[0] = 64   # replaces the value at index 0
print(nums)

# LIST METHODS
# Special built-in methods
# append adds to the end, remove deletes the first match,
# insert(index, value) adds at a position, len() counts the items

words = []

words.append("Word 1")
words.append("Word 2")
words.append("Word 3")
print(words)

words.remove("Word 1")
words.insert(0, "Word 4")
words[1] = "Word 5"
length = len(words)
print(words)
print(length)

# ITERATION
# Iteration means repeating code with a loop.

# For Loop
# A for loop will iterate over a RANGE.
# A range is a range of numbers. 
# # range(stop), range(start, stop), range( start, stop, step)
# A range stops BEFORE the stop value: range(5) gives 0, 1, 2, 3, 4
print()
for i in range(5):
    print(i)

animals = ["Sheep", "Deer", "Moose"]
print(f"List: {animals}")

# A for loop can also visit each item in a list directly.
for animal in animals:
    print(f"We saw {animal}")

nums = [5.1, 2.2, 5.3, 3.4, 8.5, 9.9]

# for n in nums:
#     print(n + 1)
#write a for loop to print each value in list nums

# range(len(nums)) gives every index, so nums[i] is each item
for i in range(len(nums)):
    print(nums[i])

# Debugging above for loop
print(len(nums))
print(range(5))


# WHILE LOOP

# iterates while a condition is true
# when the condition becomes false, it stops
# Something inside the loop must change, or the condition never becomes false.

x = 5

while x < 10:
    print(x)
    x += 1

t = True
f = False

# while t or f:
#     print('hi') # infinite loop. ctrl + c to stop it.

    
# while t and f:
#     print('hi') # condition is false. never runs