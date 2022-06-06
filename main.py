import pygame
import os

# WINDOW PROPERTIES
pygame.init()
WIDTH, HEIGHT = 800, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# COLORS
WHITE = (255, 255, 255)

# LOADING IMAGES
images = []
for num in range(7):
    image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "hangman" + str(num) + ".png")), (216, 209))
    images.append(image)

# GAME VARIABLES
FPS = 60
clock = pygame.time.Clock()
run = True
hangman_status = 6

while run:
    clock.tick(FPS)
    WINDOW.fill(WHITE)
    WINDOW.blit(images[hangman_status], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)

pygame.quit()


