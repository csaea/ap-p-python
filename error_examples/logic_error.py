# Logic errors occur when code runs without crashing but gives the wrong result.
# Typically a human error!

# Example 1: using + instead of * for area
length = 5
width = 10
area = length + width  # should be length * width
print("Area:", area)  # Wrong output

# Example 2: wrong condition in if statement
age = 20
if age > 18:
    print("Minor")
else:
    print("Adult")  # Condition should be inverted

