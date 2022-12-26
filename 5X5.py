import numpy as np

board = np.zeros((5,5), dtype=int)

def print_board(board):
    for row in board:
        print(row)

def is_game_over(board):
    # Check for a winner
    for row in range(5):
        for col in range(5):
            # Check for horizontal win
            if (row+4) <= 4 and board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == board[row+4][col] and board[row][col] != 0:
                return board[row][col]
            # Check for vertical win
            if (col+4) <= 4 and board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == board[row][col+4] and board[row][col] != 0:
                return board[row][col]
            # Check for diagonal win
            if (row+4) <= 4 and (col+4) <= 4 and board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4] and board[row][col] != 0:
                return board[row][col]
            if (row-4) >= 0 and (col+4) <= 4 and board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == board[row-4][col+4] and board[row][col] != 0:
                return board[row][col]
    # Check for a draw
    if np.all(board != 0):
        return 0
    else:
        return None

def minimax(board, depth, player):
    # Get the game status
    status = is_game_over(board)
    # If game is over, return the score
    if status is not None:
        if status == 1:
            return 1
        elif status == 2:
            return -1
        elif status == 0:
            return 0
    # Check if the board is full
    if np.all(board != 0):
        return 0
    # Check if it's player 1's turn
    if player == 1:
        best_score = -float('inf')
        for row in range(5):
            for col in range(5):
                # Check if the slot is empty
                if board[row][col] == 0:
                    # Make the move
                    board[row][col] = 1
                    # Recursively call the minimax function
                    score = minimax(board, depth+1, 2)
                    # Reset the board
                    board[row][col] = 0
                    # Check if it's the best score
                    best_score = max(score, best_score)
        return best_score
    # Check if it's player 2's turn
    elif player == 2:
        best_score = float('inf')
        for row in range(5):
            for col in range(5):
                # Check if the slot is empty
                if board[row][col] == 0:
                    # Make the move
                    board[row][col] = 2
                    # Recursively call the minimax function
                    score = minimax(board, depth+1, 1)
                    # Reset the board
                    board[row][col] = 0
                    # Check if it's the best score
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    # Find the best move
    best_score = -float('inf')
    move = (-1, -1)
    for row in range(5):
        for col in range(5):
            # Check if the slot is empty
            if board[row][col] == 0:
                # Make the move
                board[row][col] = 1
                # Recursively call the minimax function
                score = minimax(board, 0, 2)
                # Reset the board
                board[row][col] = 0
                # Check if it's the best score
                if score > best_score:
                    best_score = score
                    move = (row, col)
    # Return the best move
    return move

# Player 1 is X and Player 2 is O
player = 1
player_name = {1: 'X', 2: 'O'}

# Main loop
while True:
    # Print the board
    print_board(board)
    # Check for game over
    status = is_game_over(board)
    if status is not None:
        if status == 0:
            print('Draw!')
        else:
            print('Player {0} ({1}) wins!'.format(status, player_name[status]))
        break
    # Get the player's move
    if player == 1:
        row, col = [int(x) for x in input('Player {0} ({1}), enter your move (row, col): '.format(player, player_name[player])).split(',')]
    else:
        row, col = best_move(board)
    # Make the move
    board[row][col] = player
    # Switch players
    player = 1 if player == 2 else 2