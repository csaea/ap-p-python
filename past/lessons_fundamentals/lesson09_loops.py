# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
import time

print()
print("--- Loops in Python ---")

# The FOR-LOOP.
# A for-loop repeats for each element in a sequence (like a list or string).

animals = ["lamb", "sheep", "cow", "goose", "donkey" ]

print("\nOur animals:", animals)
print("\n--- For Loop: visiting each animal ---")

for animal in animals:
    print("Now petting a", animal)
    time.sleep(0.5)
print("\nNow I have petted all the animals.")

# We can loop through numbers using range().
print()
print("--- For Loop with range() ---")

for i in range(5):
    print("Counting:", i)

print()
print("Done counting. Well that was fun.")

# range(start, stop, step)
print()
print("--- range() with start, stop, step ---")

for num in range(2, 11, 2):
    print("Even number:", num)

print("Loop ended. Evens found.")
print()

# Strings are also iterable, so they can be looped as well!

print("--- Iterating over strings ---\n")

fav_word = "Shenanigan"

letter_list = []
print("letter_list before loop: ", letter_list)

for letter in fav_word:
    print(letter, end="") # You can use end="" to override the default new line
    letter_list.append(letter)

print("\nLetter List after loop: ", letter_list)


# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------

print()
print("--- While Loops ---")

# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 

count = 0

while count < 5:
    print(f"Loopin'. We are on loop # {count}")
    count += 1  # increase count to eventually escape
    time.sleep(0.5)

print("Escaped the loop! Freedom tastes like indentation.\n")

# Example with user input 

user_input = ""
while user_input != "exit":

    user_input = input("Type 'exit' to escape: ")

print("You have exited. Python thanks you.")
print("Resuming in 3 . . .")
time.sleep(1)
print("Resuming in 2 . . .")
time.sleep(1)
print("Resuming in 1 . . .")
time.sleep(1)
print()

count = 60
increment = 1

while count > 0:
    count -= increment

    if count < 0:
        break
    
    increment = increment + 1
    print(count)


# ---------------------------------------------------------
# Loop Control Statements
# ---------------------------------------------------------

print()
print("--- Loop Control: break, continue, pass")

for i in range(1, 11):

    if i == 3:
        print("Skipping 3.")
        continue  # skip this iteration
    if i == 6:
        print("Breaking at 6.")
        break  # stop the loop entirely
    if i == 9:
        pass # place holder. does nothing. will code in the future

    print("Number:", i)

else:
    print("Loop completed naturally.")  # only runs if not broken

print("Loop control demonstrated.")

# ---------------------------------------------------------
# NESTED LOOPS
# ---------------------------------------------------------

print()
print("--- Nested Loops ---")

# Loops inside loops: recursion’s less intelligent cousin.
# Useful for working with grids or 2D data.

counter = 0

grid = [
    [1, 2, 3], #1
    [4, 5, 6], #2
    [7, 8, 9]  #3
]

for row in grid:
    counter += 1
    print("Row:", counter)
    for value in row:
        print(value, end=" ")
    print()

print("\nThat was the grid. No surprises, just order.\n")


# ---------------------------------------------------------
# CHALLENGES
# ---------------------------------------------------------

# Challenge 1: Sum Calculator
# Use a for-loop to find the sum of numbers from 1 to 10.
# ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# Expected output: 55

# total = 0
# for i in range(1, 11):
#     total += i
# print("\nChallenge 1 - Sum of numbers 1 to 10:", total)


# Challenge 2: Guess Until Correct
# Create a while-loop that keeps asking for a number until the user types 7.

# num = 0
# while num != 7:
#     num = int(input("\nGuess a number: "))
# print("Correct. You are free to go.")


# Challenge 3: Word by Word
# Ask the user for a sentence, and print each word on a new line.
# HINT: You will have to use .split() on the sentence.

# sentence = input("\nChallenge 2 - Enter a sentence: ")
# for word in sentence.split():
#     print(word)