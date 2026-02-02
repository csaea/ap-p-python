# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

print("Functions (Procedures)")

print("\nExample 1")

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_hi()

print("\nExample 2")

def express_this(e):    # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression1 = express_this(1 + 2)    # the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression1)
expression2 = express_this(45 * 6)
print(expression2)

print("\nExample 3")

def greeter(n):       # n is the parameter
    return f"Hi {n}!"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

print("\nExample 4")

def remainder(a,b): 
    return a % b

result = remainder(3,2)
print("Remainder:", result)

print("\nExample 5")

def is_far(distance):
    # INSERT BASE CASE
    if distance < 1:
        return "Error"

    if distance >= 100:
        return "That's far"
    elif distance < 100 and distance >= 20:
        return "That's not too far"
    elif distance < 20:
        return "That's nearby!"
    
print(is_far(324))
print(is_far(55))
print(is_far(2))
print(is_far(-3))

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number

def double_sequencer(number, times):
    value = number
    sequence = []

    for i in range(times):
        value = value * 2
        sequence.append(value)
    
    return sequence

result = double_sequencer(1, 5)
print(result)
