import math
import copy

X = "X"
O = "O"
EMPTY = None


# return starting board
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Returns current player as a string
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    x_num = 0
    o_num = 0

    for row in board:
        x_num = x_num + row.count(X)
        o_num = o_num + row.count(O)

    return X if x_num == o_num else O

# returns remaining available positions on the board
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsList = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == None:
                actionsList.append((r, c))

    return actionsList

# returns new board after move
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(result_board)
    return result_board

# returns winner of the game as a string
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # checks rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != None:
            return board[i][0]
    # checks columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != None:
            return board[0][i]

    # checks diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
            return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[0][2] != None:
            return board[2][0]

    return None

# returns if the game is over
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    boardFull = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                boardFull = False
                break

    return boardFull

# returns winner of the game numerically
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Return the corresponding number to the winner's character
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    # Return if no one has won
    return 0

# returns optimal move
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    best_score = float('inf')
    best_move = None
    if current_player == X:
        best_score = float('-inf')
    
    for action in actions(board):
        new_board = result(board,action)
        
        if current_player == X:
            score = minimizer(new_board)
            if score > best_score:
                    best_score = score
                    best_move = action
        else:
            score = maximizer(new_board)
            if score < best_score:
                    best_score = score
                    best_move = action

    return best_move

def minimizer(board):
    if terminal(board):
        return utility(board)
    
    lowest_score = float("inf")
    for action in actions(board):
        new_board = result(board,action)
        score = maximizer(new_board)
        lowest_score = min(lowest_score, score)
    return lowest_score 

def maximizer(board):
    if terminal(board):
        return utility(board)
    
    highest_score = float("-inf")
    for action in actions(board):
        new_board = result(board,action)
        score = minimizer(new_board)
        highest_score = max(highest_score, score)
    return highest_score 
