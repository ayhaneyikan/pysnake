import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('PySnake')

BLUE = (0, 0, 255)
RED = (255, 0, 0)

# game logic
game_over = False
while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # if the user clicks the x button, close the window
            game_over = True
# end game logic

pygame.quit()
quit()
