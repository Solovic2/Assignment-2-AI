from connect_four_computer_algorithm import helper


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # print_hi('PyCharm')
    # import pygame

    # pygame.init()

    # win = pygame.display.set_mode((1000, 700))
    # pygame.display.set_caption("Connect Four Game")

    # x = 50
    # y = 50
    # width = 40
    # height = 60
    # vel = 5

    run = True
    game = helper()

    turn = True
    while run:
        game.print_board()
        # Player Turn
        if turn:
            x = int(input(" place : "))
            y = game.check_last_empty_cell(x)
            if y != -1:
                game.update_board(x, y,  -1)
            else:
                turn = not turn
        else:
            print('computer')
            game.get_game_leaves(1)
        turn = not turn

    # pygame.quit()

# while run:
#     pygame.time.delay(100)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT]:
#         x -= vel
#
#     if keys[pygame.K_RIGHT]:
#         x += vel
#
#     if keys[pygame.K_UP]:
#         y -= vel
#
#     if keys[pygame.K_DOWN]:
#         y += vel
#
#     win.fill((0, 0, 0))  # Fills the screen with black
#     pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#     pygame.display.update()
