import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

pygame.display.set_caption("Draw primitives")

clock = pygame.time.Clock()

done = True

while done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=False
    
    
    #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE_COLOR, [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE_COLOR, [10, 80], [320, 55])
    
    #aaline згладжена лінія, товщина в цьому
    # випадку не задається
    # pygame.draw.aaline(screen, WHITE_COLOR, [10, 70], [290, 55])
    # pygame.draw.lines(screen, YELLOW_COLOR, True, [[10, 10], [140, 70], [280, 20]], 12)
    # pygame.draw.aalines(screen, YELLOW_COLOR, False, [[10, 100], [140, 170], [280, 110]])
    
    # pygame.draw.polygon(screen, GREEN_COLOR, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    # # pygame.draw.polygon(screen, GREEN_COLOR, [[250, 110], [280, 150], [190, 190], [130, 130]])
    # pygame.draw.aalines(screen, GREEN_COLOR, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

    # pygame.draw.rect(screen, PINK_COLOR, (20, 20, 100, 75))
    # pygame.draw.rect(screen, (64, 128, 255), (150, 20, 100, 75), 8)

    # pygame.draw.circle(screen, YELLOW_COLOR, (100, 100), 50,5)
    # pygame.draw.circle(screen, PINK_COLOR, (400, 200), 50)

    # pygame.draw.ellipse(screen, GREEN_COLOR, (10, 50, 280, 100))
    pygame.display.update()