import random

random_num = random.randint(1, 9)

guess_taken = 0

print("\nA random number from 1 to 9 has been randomly generated.")
print("Keep guessing until you guessed right! Type 'exit' to quit.")

guessing = True

while guessing:

    guess = (input("\nEnter a number: "))

    if guess == "exit":
        break

    guess = int(guess)

    guess_taken = guess_taken + 1

    if guess < random_num:
        print("Your guess was too low. Try again.")
    elif guess > random_num:
        print("Your guess was too high. Try again.")
    elif guess == random_num:
        print("You got it correct!")

    if guess == random_num:
        guessing = False

print(f"You took {guess_taken} guesses.")
