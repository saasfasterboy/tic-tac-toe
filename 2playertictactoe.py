def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-|-|-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-|-|-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner(board):
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    else:
        return False

def check_tie(board):
    for i in board:
        if i == " ":
            return False
    return True

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    while True:
        print_board(board)
        move = input("Player " + player + ", make your move (1-9): ")
        move = int(move) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = player
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            return
        if check_tie(board):
            print_board(board)
            print("Tie game.")
            return
        if player == "X":
            player = "O"
        else:
            player = "X"

play_game()
