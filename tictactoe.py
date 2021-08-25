
""" Refernence from Quazi team but with all understanding this tictactoe is built
"""

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
game_still_on = True
winner = None
current_player = "X"
def display_board():
    print(board[0], " | ", board[1], " | ", board[2])
    print(board[3], " | ", board[4], " | ", board[5])
    print(board[6], " | ", board[7], " | ", board[8])
def play_game():
    display_board()
    global winner
    global game_still_on
    while game_still_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose the position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose the position from 1-9: ")
        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("Go again.")

    board[position] = player
    display_board()
def check_if_game_over():
    check_for_win()
    check_if_tie()
def check_for_win():
    global winner
    row_winner = check_row()
    coloumn_winner = check_coloumn()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
def check_diagonal():
    global game_still_on
    diagonal1 = board[0] == board[4] == board[8] != "_"
    diagonal2 = board[2] == board[4] == board[6] != "_"
    if diagonal1 or diagonal2:
        game_still_on = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return
def check_row():
    global game_still_on
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_still_on = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_coloumn():
    global game_still_on
    coloumn1 = board[0] == board[3] == board[6] != "_"
    coloumn2 = board[1] == board[4] == board[7] != "_"
    coloumn3 = board[2] == board[5] == board[8] != "_"

    if coloumn1 or coloumn2 or coloumn3:
        game_still_on = False
    if coloumn1:
        return board[0]
    elif coloumn2:
        return board[1]
    elif coloumn3:
        return board[2]
    return


def check_if_tie():
    global  game_still_on
    if "_" not in board:
        game_still_on = False
    return
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()