from Errors import SymbolError
from collections import deque


def take_manes ():
    player1 = input("Player one name: ")
    player2 = input("Player two name: ")
    while True:
        try:
            sign1 = input(f"{player1} would you like to play with 'X' or 'O'? ").upper()
            if sign1 not in {"X", "O"}:
                raise SymbolError("Please insert valid sign!")
            break
        except SymbolError as error:
            print(error)

    if sign1 == "X":
        sign2 = 'O'
    else:
        sign2 = "X"
    return (player1, sign1), (player2, sign2)


def draw_board(players):
    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")
    print(f"{players[0][0]} starts first!")


def is_free_position(position, board, sign):
    if position == 1 and board[0][0] == " ":
        board[0][0] = sign
        return True
    elif position == 2 and board[0][1] == " ":
        board[0][1] = sign
        return True
    elif position == 3 and board[0][2] == " ":
        board[0][2] = sign
        return True
    elif position == 4 and board[1][0] == " ":
        board[1][0] = sign
        return True
    elif position == 5 and board[1][1] == " ":
        board[1][1] = sign
        return True
    elif position == 6 and board[1][2] == " ":
        board[1][2] = sign
        return True
    elif position == 7 and board[2][0] == " ":
        board[2][0] = sign
        return True
    elif position == 8 and board[2][1] == " ":
        board[2][1] = sign
        return True
    elif position == 9 and board[2][2] == " ":
        board[2][2] = sign
        return True
    else:
        return False


def play_turn(board, player):
    while True:
        try:
            position = int(input(f"{player[0]} choose a free position [1-9]: "))
            if position < 1 or position > 9:
                raise SymbolError("Please insert valid number!")
            if is_free_position(position, board, player[1]):
                break
            else:
                raise SymbolError("Please insert valid number!")
        except SymbolError as error:
            print(error)
        except ValueError:
            print("Please insert only numbers!")


def print_board(board):
    for row in range(len(board)):
        print(f"| {board[row][0]} | {board[row][1]} | {board[row][2]} |")


def is_win(board, sign):
    # horizontal
    for r in board:
        if r[0] == r[1] == r[2] == sign:
            return True

    # vertical
    for c in range(len(board)):
        if board[0][c] == board[1][c] == board[2][c] == sign:
            return True

    # first diagonal
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    # second diagonal
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False


def play(players, board):
    queue = deque(players)
    count = 1
    while count < 10:

        player_turn = queue.popleft()
        queue.append(player_turn)
        play_turn(board, player_turn)
        print_board(board)
        if is_win(board, player_turn[1]):
            print(f"{player_turn[0]} won!")
            break
        count += 1

    if count == 10:
        print("Draw")


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

players = take_manes()
draw_board(players)
play(players, board)
