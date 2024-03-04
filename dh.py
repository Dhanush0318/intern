import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return row[0]

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    # Check for tie
    if all([cell != '-' for row in board for cell in row]):
        return 'Tie'

    return None

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)
    if winner:
        if winner == 'X':
            return -10 + depth, None
        elif winner == 'O':
            return 10 - depth, None
        else:
            return 0, None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval, _ = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (i, j)
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval, _ = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    if eval < min_eval:
                        min_eval = eval
                        best_move = (i, j)
        return min_eval, best_move

def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Let's play Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != '-':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"Congratulations! {winner} wins!")
            break

        # AI's move
        print("AI's move:")
        _, ai_move = minimax(copy.deepcopy(board), 0, True)
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"AI wins!")
            break

play_game()   