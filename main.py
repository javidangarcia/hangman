import pygame
import os
import math
import random
from constants import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

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
A = 65
for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letter = A + i
    letters.append([x, y, chr(letter), True])

# GAME VARIABLES
hangman_status = 0
word = random.choice(words)
guessed = []

# GAME FUNCTIONS
def draw():
    WINDOW.fill(GREEN)
    title = TITLE_FONT.render("HANGMAN", 1, BLACK)
    WINDOW.blit(title, (WIDTH / 2 - title.get_width() / 2, 20))

    # Drawing Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    WINDOW.blit(text, (280, 200))

    # Drawing Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(WINDOW, BLACK, (x, y), RADIUS, 3)
            text = BUTTON_FONT.render(ltr, 1, BLACK)
            WINDOW.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    WINDOW.blit(images[hangman_status], (25, 80))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    WINDOW.fill(GREEN)
    text = WORD_FONT.render(message, 1, BLACK)
    WINDOW.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

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
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You Won!")
            break

        if hangman_status == 6:
            display_message("You Lost!")
            break

if __name__ == "__main__":
    main()
pygame.quit()
