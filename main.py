def print_board(board_to_print):
    for i in range(3):
        for j in range(3):
            print(f" {board_to_print[i][j]} ", end="")
            if j != 2:
                print("|", end="")
        if i != 2:
            print("\n-----------")


def check_row_column_entry(board_row, board_column):
    if 0 > board_row or board_row > 2 or 0 > board_column or board_column > 2:
        return False
    else:
        return True


def cell_filled_with(board_row, board_column):
    return board[board_row][board_column]


def insert_symbol(player_on_turn, board_row, board_column):
    cell_symbol = cell_filled_with(board_row, board_column)
    if cell_symbol == "X" or cell_symbol == "O":
        return False
    if player_on_turn == player_one:
        symbol = "X"
    else:
        symbol = "O"
    board[board_row][board_column] = symbol
    return True


def check_winner(symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True

    for j in range(3):
        if board[0][j] == symbol and board[1][j] == symbol and board[2][j] == symbol:
            return True

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False


def game_won(player_on_turn):
    if player_on_turn == player_one:
        symbol = "X"
    else:
        symbol = "O"

    return check_winner(symbol)


def initialize_board():
    return [[" " for i in range(3)] for j in range(3)]


def change_turn(player_on_turn):
    if player_on_turn == player_one:
        return player_two
    else:
        return player_one


def play_game(player_on_turn):
    global board
    board = [[" " for i in range(3)] for j in range(3)]
    print(f"{player_on_turn} goes first")
    game_over = False

    while not game_over:
        repeat_entry = True
        cell_filled = False
        print("\n------------\n")
        print(f" {player_on_turn}'s turn:\n")
        print_board(board)
        print(f" \n\n{player_on_turn}, enter row and column where you want to put your symbol")
        while repeat_entry or cell_filled:
            try:
                row = int(input("Row: ")) - 1
                column = int(input("Column: ")) - 1
            except ValueError:
                print("Wrong input, please try again.")
                continue
            repeat_entry = not check_row_column_entry(row, column)
            if repeat_entry:
                print("Wrong input, please try again.")
                continue
            cell_filled = not insert_symbol(player_on_turn, row, column)
            if cell_filled:
                print("Cell already filled, please try again.")
                continue
        game_over = game_won(player_on_turn)
        if not game_over:
            player_on_turn = change_turn(player_on_turn)
    return player_on_turn


board = []
print("Welcome to the Tic Tac Toe multiplayer game!")
print("Please enter the name of player 1:")
player_one = input()
print("Please enter the name of player 2:")
player_two = input()
print(f"\n{player_one} is X")
print(f"{player_two} is O")

player_one_wins = 0
player_two_wins = 0
first_turn = player_one
exit_game = False

while not exit_game:
    print(f"\nGame {player_one_wins + player_two_wins + 1}")
    print(f"Score is: {player_one_wins}-{player_two_wins}")
    winner = play_game(first_turn)
    print(f"\n{winner} has won the game!")
    if winner == player_one:
        player_one_wins += 1
    else:
        player_two_wins += 1
    another_game = input("To play another game enter Y and to exit game enter any key: ").upper()
    if another_game != "Y":
        exit_game = True
    first_turn = change_turn(first_turn)


