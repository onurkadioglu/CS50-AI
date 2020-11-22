"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # If Initial state, X turn
    if board == initial_state():
        return X

    # If X_num > O_num, O turn
    X_num = 0
    O_num = 0
    for row in board:
        for cell in row:
            if cell == X:
                X_num += 1
            if cell == O:
                O_num += 1

    if X_num > O_num:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If action isn't valid, raise Exception
    if action not in actions(board):
        raise Exception("Illegal Move")

    returned_board = copy.deepcopy(board)
    returned_board[action[0]][action[1]] = player(board)
    return returned_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Column check
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] is not None:
            if board[0][i] == X:
                return X
            elif board[0][i] == O:
                return O
            else:
                return None

    # Row check
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] is not None:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None

    # Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] is not None:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None

    if board[2][0] == board[1][1] == board[0][2] is not None:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If there is a winner
    if winner(board) is not None:
        return True

    # If all cells have been filled
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        value = 1
    elif winner(board) == O:
        value = -1
    else:
        value = 0

    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)

    if turn == X:
        value = float('-inf')
        for action in actions(board):
            res = min_value(result(board, action))
            if res > value:
                value = res
                best_move = action

    elif turn == O:
        value = float('inf')
        for action in actions(board):
            res = max_value(result(board, action))
            if res < value:
                value = res
                best_move = action
    return best_move

def max_value(board):

    if terminal(board):
        return utility(board)

    value = float('-inf')

    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):

    if terminal(board):
        return utility(board)

    value = float('inf')

    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
