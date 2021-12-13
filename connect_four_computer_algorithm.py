import numpy as np


class helper:
    def __init__(self):
        self.board = np.zeros((6, 7), int)
        self.row = 6
        self.col = 7

    def print_board(self):
        print(self.board)

    # update board
    def update_board(self, x, y, player_move):
        self.board[y][x] = player_move

    # check last empty cell in column
    def check_last_empty_cell(self, state, x):
        for index in range(self.row-1, -1, -1):
            if state[index][x] == 0:
                return index
        return -1

    # check all possible places for minimax
    def get_game_leaves(self, state, value):
        successors = []
        for index in range(self.col):
            check_cell = self.check_last_empty_cell(state,index)
            if check_cell != -1:
                possible_game = state.copy()
                possible_game[check_cell][index] = value
                successors.append(possible_game)
        return successors

    def maximize(self,depth,state):
        successor = self.get_game_leaves(state,1)
        if len(successor) == 0 or depth == 0:
            # Evaluate
            print()
        else:
            for state in successor:
                minimize(depth-1,state)


