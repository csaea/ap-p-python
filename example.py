import random

running = True

while running:
    answer = input("Want to play a game? (yes/no): ").lower()

    if answer == "no":
        print("Goodbye!")
        running = False
    elif answer == "yes":

        target = random.randint(1, 10)
        guess = None

        while guess != target:
            guess = int(input("Guess a number from 1 to 10: "))

        print("You got it!")
    else:
        print("Please type yes or no.")