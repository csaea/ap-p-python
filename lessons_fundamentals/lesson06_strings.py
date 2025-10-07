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
print("Length:", length)

# If you want to concatenate a number, you must cast it to a string with str() 
print("The last name is" + str(length) + "letters long")

character = "spOngEBOB SQuarPaNts"
print("\nUppercase:", character.upper())
print("Lowercase:", character.lower())
print("Capitalized first letter:", character.capitalize())
print("Title Format:", character.title())