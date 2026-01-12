def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Check for valid bounds
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Error: Row and column must be between 0 and 2. Try again.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                moves += 1
                
                # Check for draw condition (9 moves with no winner)
                if moves == 9:
                    print_board(board)
                    print("It's a draw!")
                    return
                
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers between 0 and 2.")
            continue

    print_board(board)
    # Switch player back since the winner is the one who just moved
    if player == "X":
        player = "O"
    else:
        player = "X"
    print("Player " + player + " wins!")

tic_tac_toe()