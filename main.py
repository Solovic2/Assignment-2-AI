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


def win_status():
    white = (255, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 32)
    who_wins = " DRAW ... "
    if score > 0:
        who_wins = "Game Over , Computer Beats you LOSER !!"
    else:
        who_wins = "Congratulation , You Beats This Machine  !!"

    text = font.render(who_wins, True, (0, 0, 0))
    text_rect = text.get_rect()

    # set the center of the rectangular object.
    text_rect.center = (350, 350)

    # infinite loop
    while True:

        # Fill Screen With White Color
        win.fill(white)
        # Display Text
        win.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()

            # Draws the surface object to the screen.
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
    score = 0
    while run:
        draw_board(game.board)
        score = game.evaluate(game.board)
        print(score)

        if turn:
            x = move()
            print("X from GUI {}".format(x))
            y = game.check_last_empty_cell(game.board, x)
            if x == -1:
                break
            if y != -1:
                game.update_board(x, y, game.PLAYER)
            else:
                turn = not turn
        else:
            tree = {}
            score, next_state = game.maximize_alpha_beta_pruning(2, game.board, -math.inf, math.inf, tree)
            game.board = next_state
            print(tree)
            count = 0
            for i in range(len(tree)):
                count += len(tree[i])
            print("\n Number Of Nodes is : {} \n".format(count))
        turn = not turn

        if game.game_over():
            run = False
    win_status()
    pygame.quit()
