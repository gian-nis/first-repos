
import random

b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

random_number = random.choice(b)
random_number2 = random.choice(b)
random_number3 = random.choice(b)
random_number4 = random.choice(b)

number = random_number + random_number2 + random_number3 + random_number4

game_active = True

idx = 0

c = 0

while game_active:

    guess = input("Guess a 4-digit number with spaces in between: ")

    for i in guess:
        if i == number[idx]:
            print("Cow")
        elif i in number:
            print("Bull")
        idx = idx + 1

    c += 1
    idx = 0

    if guess == number:
        print(f"Congrats you guessed correctly! It took you {c} tries.")
        game_active = False

