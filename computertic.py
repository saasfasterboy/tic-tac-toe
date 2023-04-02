import random

def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def player_move(board, player):
    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and int(move) >= 0 and int(move) <= 8 and board[int(move)] == " ":
            board[int(move)] = player
            break
        else:
            print("Invalid move. Try again.")
    print_board(board)

def computer_move(board, computer, human):
    print("Computer's turn")
    for i in range(9):
        if board[i] == " ":
            board[i] = computer
            if check_win(board, computer):
                print_board(board)
                print("Computer wins!")
                return
            else:
                board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = human
            if check_win(board, human):
                board[i] = computer
                print_board(board)
                print("Computer's move: " + str(i))
                return
            else:
                board[i] = " "
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = computer
            print_board(board)
            print("Computer's move: " + str(move))
            break

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(board)
    while True:
        player_move(board, "X")
        if check_win(board, "X"):
            print("You win!")
            return
        if " " not in board:
            print("Tie!")
            return
        computer_move(board, "O", "X")
        if check_win(board, "O"):
            print("Computer wins!")
            return

play_game()
