import pygame
import sys

# Initialisierung
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("physics demo")

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Quadratgröße
SQUARE_SIZE = 20

# Hauptschleife
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Mausposition
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Quadrat zeichnen (zentriert auf Maus)
    square_rect = pygame.Rect(
        mouse_x - SQUARE_SIZE // 2,
        mouse_y - SQUARE_SIZE // 2,
        SQUARE_SIZE,
        SQUARE_SIZE
    )
    pygame.draw.rect(screen, RED, square_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
