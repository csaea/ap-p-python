# Basic string creation and indexes:
greeting = "Hello"
first_name = "Ada"
print(greeting, first_name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

#Concatenation: 
message = greeting + " " + first_name + "!!!!"
print("Concatenated message:", message)

print()
#Splicing
word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters (non-inclusive):", word[-7:-2])
print(word[:5])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

## Built-in string functions

last_name = "Lovelace"
length = len(last_name)
print("Length of name:", length)

character = "spOngEBOB SQuarePaNts"
print("\nUppercase:", character.upper())
print("Lowercase:", character.lower())
print("Capitalized first letter:", character.capitalize())
print("Title Format:", character.title())

print()

#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
next_replacement = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(next_replacement)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Adam"
age = 400
city = "Valhalla"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

