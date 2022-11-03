import pygame

def log(text : str) -> None :
    """log text
    Args:
        text (str): Uwu
    """
    print(text)
    
def display_text(text : str, screen : pygame.Surface) -> None :
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, (25, 5, 0), (5, 89, 2))
    screen.blit(text, (50, 90, 200, 0))