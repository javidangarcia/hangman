import pygame

# GAME VARIABLES
WIDTH, HEIGHT = 800, 500
FPS = 60

# COLORS
GREEN = (86, 174, 87)
BLACK = (0, 0, 0)

# FONTS
pygame.init()
BUTTON_FONT = pygame.font.SysFont("comicsans", 35)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 40)

# WORDS
words = ["PYTHON", "COMPUTER", "GOOGLE", "MICROSOFT", "JAVA", "APPLE", "SOFTWARE", "PYGAME",\
         "BOOLEAN", "ARRAY", "HASHMAP", "ALGORITHM", "FACEBOOK", "AMAZON", "STRING", "FRAMEWORK",\
         "PROGRAMMING", "DEVELOPER", "GITHUB", "TECHNOLOGY", "RECURSION", "QUEUE", "STACK"]