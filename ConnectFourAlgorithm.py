import math

import numpy as np


class helper:
    def __init__(self):
        self.board = np.zeros((6, 7), int)
        self.row = 6
        self.col = 7
        self.AGENT = 1
        self.PLAYER = -1
        self.TWO = 10
        self.THREE = 100
        self.FOUR = 100000

    def print_board(self):
        print(self.board)

    # update board
    def update_board(self, x, y, player_move):
        self.board[y][x] = player_move

    def game_over(self):
        for i in range(self.col):
            if self.board[0][i] == 0:
                return False
        return True

    # check last empty cell in column
    def check_last_empty_cell(self, state, x):
        for index in range(self.row - 1, -1, -1):
            if state[index][x] == 0:
                return index
        return -1

    # check all possible places for minimax
    def get_game_leaves(self, state, value):
        successors = []
        for index in range(self.col):
            check_cell = self.check_last_empty_cell(state, index)
            if check_cell != -1:
                possible_game = state.copy()
                possible_game[check_cell][index] = value
                successors.append(possible_game)
        return successors

    def maximize(self, depth, state, tree={}):
        successor = self.get_game_leaves(state, self.AGENT)
        if len(successor) == 0 or depth == 0:
            value = self.evaluate(state)
            if depth in tree:
                tree[depth].append((state, value))
            else:
                tree[depth] = [(state, value)]

            return value, state
        else:
            if depth in tree:
                tree[depth].append(state)
            else:
                tree[depth] = [state]
            max_score = -math.inf
            max_state = None

            for state in successor:
                next_score, next_state = self.minimize(depth - 1, state, tree)
                if next_score > max_score:
                    max_score = next_score
                    max_state = state

        return max_score, max_state

    def minimize(self, depth, state, tree={}):
        successor = self.get_game_leaves(state, self.PLAYER)
        if len(successor) == 0 or depth == 0:
            value = self.evaluate(state)
            if depth in tree:
                tree[depth].append((state, value))
            else:
                tree[depth] = [(state, value)]

            return value, state
        else:
            if depth in tree:
                tree[depth].append(state)
            else:
                tree[depth] = [state]
            min_score = math.inf
            min_state = None

            for state in successor:
                next_score, next_state = self.maximize(depth - 1, state, tree)
                if next_score < min_score:
                    min_score = next_score
                    min_state = state

        return min_score, min_state

    # maximize with alpha-beta pruning
    def maximize_alpha_beta_pruning(self, depth, state, alpha, beta, tree={}):
        successor = self.get_game_leaves(state, self.AGENT)
        if len(successor) == 0 or depth == 0:
            value = self.evaluate(state)
            if depth in tree:
                tree[depth].append((state, value))
            else:
                tree[depth] = [(state, value)]

            return value, state
        else:
            if depth in tree:
                tree[depth].append(state)
            else:
                tree[depth] = [state]
            max_score = -math.inf
            max_state = None

            for state in successor:
                next_score, next_state = self.minimize_alpha_beta_pruning(depth - 1, state, alpha, beta,tree)
                if next_score > max_score:
                    max_score = next_score
                    max_state = state
                if max_score >= beta:
                    break
                if max_score > alpha:
                    alpha = max_score
        return max_score, max_state

    # minimize with alpha-beta pruning
    def minimize_alpha_beta_pruning(self, depth, state, alpha, beta, tree={}):
        successor = self.get_game_leaves(state, self.PLAYER)
        if len(successor) == 0 or depth == 0:
            value = self.evaluate(state)
            if depth in tree:
                tree[depth].append((state, value))
            else:
                tree[depth] = [(state, value)]

            return value, state
        else:
            if depth in tree:
                tree[depth].append(state)
            else:
                tree[depth] = [state]
            min_score = math.inf
            min_state = None

            for state in successor:
                next_score, next_state = self.maximize_alpha_beta_pruning(depth - 1, state, alpha, beta,tree)
                if next_score < min_score:
                    min_score = next_score
                    min_state = state
                if min_score <= alpha:
                    break
                if min_score < beta:
                    beta = min_score
        return min_score, min_state

    def evaluate(self, board):
        score = 0

        for i in range(self.row):
            countMax = 0
            countMin = 0

            for j in range(self.col):

                if board[i][j] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[i][j] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

        for i in range(self.col):
            countMax = 0
            countMin = 0

            for j in range(self.row):

                if board[j][i] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[j][i] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        for i in range(self.col):
            countMax = 0
            countMin = 0

            r = 0
            c = i

            while r < self.row and c < self.col:
                if board[r][c] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[r][c] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

                r = r + 1
                c = c + 1

        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        for i in range(1, self.row):
            countMax = 0
            countMin = 0

            r = i
            c = 0

            while r < self.row and c < self.col:
                if board[r][c] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[r][c] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

                r = r + 1
                c = c + 1

        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        for i in range(self.col - 1, -1, -1):
            countMax = 0
            countMin = 0

            r = 0
            c = i

            while r < self.row and c < self.col:
                if board[r][c] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[r][c] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

                r = r + 1
                c = c - 1

        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        for i in range(1, self.row):
            countMax = 0
            countMin = 0

            r = i
            c = self.col - 1

            while r < self.row and c < self.col:
                if board[r][c] == self.AGENT:
                    countMax += 1
                    countMin = 0
                elif board[r][c] == self.PLAYER:
                    countMin += 1
                    countMax = 0
                else:
                    countMin = 0
                    countMax = 0

                if countMax == 2:
                    score += self.TWO
                elif countMax == 3:
                    score += self.THREE
                elif countMax >= 4:
                    score += self.FOUR

                if countMin == 2:
                    score -= (self.TWO + 5)
                elif countMin == 3:
                    score -= (self.THREE + 50)
                elif countMin >= 4:
                    score -= (self.FOUR + 50)

                r = r + 1
                c = c - 1

        return score
