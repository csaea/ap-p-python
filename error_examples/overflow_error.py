# Python floats are 64-bit (double precision). 
# Using powers of 10 can show the limits of float representation.

# This fits within 64 bits:
x = 10.0 ** 308
print(x)

# This exceeds 64-bit float capacity:
y = 10.0 ** 309
print(y)  # Results in 'inf'

# Fun fact: Python integers never overflow; they grow in size as needed.
