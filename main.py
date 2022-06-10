import pygame
import os
import math

# WINDOW PROPERTIES
pygame.init()
WIDTH, HEIGHT = 800, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")
BUTTON_FONT = pygame.font.SysFont("comicsans", 35)

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# LOADING IMAGES
images = []
for num in range(7):
    image = pygame.transform.scale(pygame.image.load(os.path.join("assets", "hangman" + str(num) + ".png")), (216, 209))
    images.append(image)

# BUTTON VARIABLES
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 370
a = 65
for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letter = a + i
    letters.append([x, y, chr(letter), True])

# GAME VARIABLES
FPS = 60
clock = pygame.time.Clock()
hangman_status = 1

# GAME FUNCTIONS
def draw():
    WINDOW.fill(WHITE)

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(WINDOW, BLACK, (x, y), RADIUS, 3)
            text = BUTTON_FONT.render(ltr, 1, BLACK)
            WINDOW.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    WINDOW.blit(images[hangman_status], (40, 80))
    pygame.display.update()

def main():
    run = True
    while run:
        clock.tick(FPS)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt( math.pow(x - mouse_x, 2) + math.pow(y - mouse_y, 2) )
                        if distance < RADIUS:
                            letter[3] = False

    pygame.quit()

main()

