import pygame
import sys
import random

boxes = []
# Initialisierung
pygame.init()

# Create Matrix

# Fenstergröße
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("physics demo")
clock = pygame.time.Clock()

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)
mouse_clicked = False
# Quadratgröße
SQUARE_SIZE = 16

# Hauptschleife
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("ii")
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

        # Maustaste losgelassen
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked = False
    # Mausposition
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Quadrat zeichnen (zentriert auf Maus)
    square_rect = pygame.Rect(
        mouse_x - SQUARE_SIZE // 2,
        mouse_y - SQUARE_SIZE // 2,
        SQUARE_SIZE,
        SQUARE_SIZE
    )
    sand_box = pygame.Rect(
        round((mouse_x - SQUARE_SIZE // 2)/16)*16,
        round((mouse_y - SQUARE_SIZE // 2)/16)*16,
        SQUARE_SIZE,
        SQUARE_SIZE
    )
    if mouse_clicked:
        boxes.append([sand_box, (random.randint(0,255), random.randint(0,255), random.randint(0,255))])
    pygame.draw.rect(screen, RED, square_rect)
    for i in boxes:
        rect = pygame.Rect(
            i[0[0]],
            i[0[1]],
            i[0[2]],
            i[0[2]]
        )
        pygame.draw.rect(screen, i[1], i[0])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
