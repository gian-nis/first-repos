
score1 = 0
score2 = 0

active_game = True

while active_game:

    player1 = input("\nPlayer 1, choose rock, paper, or scissors: ")
    player2 = input("Player 2, choose rock, paper, or scissors: ")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "paper":
        print("Player 2 wins!")
        score2 = score2 + 1
    elif player1 == "paper" and player2 == "scissors":
        print("Player 2 wins!")
        score2 = score2 + 1
    elif player1 == "scissors" and player2 == "rock":
        print("Player 2 wins!")
        score2 = score2 + 1
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
        score1 = score1 + 1
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
        score1 = score1 + 1
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
        score1 = score1 + 1

    print(f"\nPlayer 1: {score1}\nPlayer 2: {score2}\n")

    proceed = input("Do you want to do another round? (Y/N)  ")

    if proceed == "N":
        active_game = False
