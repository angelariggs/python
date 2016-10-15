import random

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}."

print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("Guess the magic number.")
    guess = int(input())
    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print("Your guess is too low; please guess again.")
    if guess > magicNumber:
        print("Your guess is too high; please guess again.")
print("You guessed the magic number!")
