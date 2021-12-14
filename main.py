import math

import pygame

from connect_four_computer_algorithm import helper


def draw_board(board):
    pygame.draw.rect(win, (0, 0, 153), (0, scale, 700, 600))

    for r in range(6):
        for c in range(7):
            if board[r][c] == -1:
                pygame.draw.circle(win, (255, 0, 0), (int(c * scale + scale / 2), int(r * scale + scale + scale / 2)),
                                   radius)
            elif board[r][c] == 1:
                pygame.draw.circle(win, (255, 255, 0), (int(c * scale + scale / 2), int(r * scale + scale + scale / 2)),
                                   radius)
            else:
                pygame.draw.circle(win, (0, 0, 0), (int(c * scale + scale / 2), int(r * scale + scale + scale / 2)),
                                   radius)
    pygame.display.update()


def move():
    pos = scale / 2
    while True:
        pygame.draw.circle(win, (255, 0, 0), (int(pos), int(scale / 2)), radius)
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and pos > 50:
            pygame.draw.rect(win, (0, 0, 0), (0, 0, 700, 100))
            pos -= scale
            pygame.draw.circle(win, (255, 0, 0), (int(pos), int(scale / 2)), radius)
        if keys[pygame.K_RIGHT] and pos < 650:
            pygame.draw.rect(win, (0, 0, 0), (0, 0, 700, 100))
            pos += scale
            pygame.draw.circle(win, (255, 0, 0), (int(pos), int(scale / 2)), radius)
        if keys[pygame.K_DOWN]:
            pygame.draw.rect(win, (0, 0, 0), (0, 0, 700, 100))
            pygame.display.update()
            return int((pos - 50) / 100)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Connect Four Game")
    game = helper()
    scale = 100
    height = (game.row + 1) * scale
    radius = 40

    run = True
    turn = True
    while run:
        game.print_board()
        draw_board(game.board)
        score = game.evaluate(game.board)
        print(score)

        if turn:
            # x = int(input(" place : "))
            x = move()
            print("X from GUI {}".format(x))
            y = game.check_last_empty_cell(game.board, x)
            if y != -1 and x != -1:
                game.update_board(x, y, game.PLAYER)
            else:
                turn = not turn
        else:
            score, next_state = game.maximize_alpha_beta_pruning(3, game.board, -math.inf, math.inf)
            game.board = next_state
        turn = not turn

        if game.game_over():
            run = False
    pygame.quit()
