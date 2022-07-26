"""
Tic Tac Toe Player
"""

import math
import copy
import time

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
    if board == initial_state():
        return X
    none = 0
    for x, y in enumerate(board):
        for a, b in enumerate(y):
            if b is None:
                none += 1
    if none % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    baord2 = copy.deepcopy(board)
    for x, y in enumerate(baord2):
        for a, b in enumerate(y):
            if b is None:
                options.add((x, a))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        return NameError("Action cannot be performed.")
    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)
    return board2


def winner(board):
    # if board[0][0] == board[1][1] == board[2][2]:
    #     win = board[0][0]
    # elif board[0][0] == board[0][1] == board[0][2]:
    #     win = board[0][0]
    # elif board[1][0] == board[1][1] == board[1][2]:
    #     win = board[1][0]
    # elif board[2][0] == board[2][1] == board[2][2]:
    #     win = board[2][0]
    # elif board[0][0] == board[1][0] == board[2][0]:
    #     win = board[0][0]
    # elif board[0][1] == board[1][1] == board[2][1]:
    #     win = board[0][1]
    # elif board[0][2] == board[1][2] == board[2][2]:
    #     win = board[0][2]
    # elif board[0][2] == board[1][1] == board[2][0]:
    #     win = board[0][2]
    # else:
    #     win = None
    # return win

    if (board[1][1] == board[0][0]) and (board[1][1] == board[2][2]) or (board[1][1] == board[0][2]) and (
            board[1][1] == board[2][0]) \
            or (board[1][1] == board[1][0]) and (board[1][1] == board[1][2]) or (board[1][1] == board[0][1]) and (
            board[1][1] == board[2][1]):
        win = board[1][1]
    elif (board[0][1] == board[0][0]) and (board[0][1] == board[0][2]):
        win = board[0][1]
    elif (board[2][1] == board[2][0]) and (board[2][1] == board[2][2]):
        win = board[2][1]
    elif (board[1][0] == board[0][0]) and (board[1][0] == board[2][0]):
        win = board[1][0]
    elif (board[1][2] == board[0][2]) and (board[1][2] == board[2][2]):
        win = board[1][2]
    else:
        win = None
    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        options = actions(board)
        optionlist = []
        valuelist = []

        for option in options:
            valuelist.append(minValue(result(board, option)))
            optionlist.append(option)

        return optionlist[valuelist.index(max(valuelist))]

    elif player(board) == O:
        options = actions(board)
        optionlist = []
        valuelist = []

        for option in options:
            valuelist.append(maxValue(result(board, option)))
            optionlist.append(option)

        return optionlist[valuelist.index(min(valuelist))]


def minValue(board):
    if terminal(board):
        a = utility(board)
        return a
    else:
        v = 100
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))
        return v


def maxValue(board):
    if terminal(board):
        a = utility(board)
        return a
    else:
        v = -100
        for action in actions(board):
            v = max(v, minValue(result(board, action)))
        return v
