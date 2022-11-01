from source.background import log, display_text
import pygame

pygame.init()

screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption(
    "The Hime GAAMMMEE UWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWUUWU")


running = True

background = False

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYUP:
            
            log("Uwu")
            background = True

    if background != True:

        screen.fill((0, 58, 30))
        pygame.draw.circle(screen, (0, 88, 255), (500, 250), 50)

    else:

        screen.fill((255, 58, 30))
        pygame.draw.rect(screen, (60, 133, 38), (0, 20, 300, 300))
        display_text("Uwu", screen)

    pygame.display.flip()

pygame.quit()