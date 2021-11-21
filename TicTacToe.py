game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board():

    print(f' --- ' + "--- " + "--- ")
    print(f'| {game[0][0]} |' + f" {game[0][1]} |" + f" {game[0][2]} |")
    print(f' --- ' + "--- " + "--- ")
    print(f'| {game[1][0]} |' + f" {game[1][1]} |" + f" {game[1][2]} |")
    print(f' --- ' + "--- " + "--- ")
    print(f'| {game[2][0]} |' + f" {game[2][1]} |" + f" {game[2][2]} |")
    print(f' --- ' + "--- " + "--- ")


game_active = True

idx = 0
game_turn = 0
stop_game = 0

while game_active:

    print("\n")

    game_board()

    print("\n")

    one_x_axis = int(input("Player One, enter the x for the space that you want: "))
    one_x_adjust = one_x_axis - 1
    one_y_axis = int(input("Player One, Enter the y for the space that you want: "))
    one_y_adjust = one_y_axis - 1

    game[one_y_adjust][one_x_adjust] = 1

    game_turn += 1

    if game_turn == 9:
        print("It's a tie!")
        game_board()
        break

    for i in range(0, 3):   # checks vertical rows
        if game[0][i] == 1 and game[1][i] == 1 and game[2][i] == 1:
            print("\nPlayer One Wins!")
            stop_game = 1

    for i in range(0, 3):   # checks horizontal rows
        if game[i][0] == 1 and game[i][1] == 1 and game[i][2] == 1:
            print("\nPlayer One Wins!")
            stop_game = 1

    if game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:   # checks vertically to down-right
        print("\nPlayer One Wins!")
        stop_game = 1

    if game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1:   # checks vertically to down-left
        print("\nPlayer One Wins!")
        stop_game = 1

    if stop_game == 1:
        game_board()
        break

    print("\n")

    game_board()

    print("\n")

    two_x_axis = int(input("Player Two, enter the x for the space that you want: "))
    two_x_adjust = two_x_axis - 1
    two_y_axis = int(input("Player Two, Enter the y for the space that you want: "))
    two_y_adjust = two_y_axis - 1

    game[two_y_adjust][two_x_adjust] = 2

    game_turn += 1

    for i in range(0, 3):
        if game[0][i] == 2 and game[1][i] == 2 and game[2][i] == 2:
            print("\nPlayer Two Wins!")
            stop_game = 1

    for i in range(0, 3):
        if game[i][0] == 2 and game[i][1] == 2 and game[i][2] == 2:
            print("\nPlayer Two Wins!")
            stop_game = 1

    if game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
        print("\nPlayer Two Wins!")
        stop_game = 1

    if game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
        print("\nPlayer Two Wins!")
        stop_game = 1

    if stop_game == 1:
        game_board()
        break

