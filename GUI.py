# GUI.py
import sys
import pygame
import pygame_gui

SCREEN_WIDTH_HEIGHT = 800
CLOCK = pygame.time.Clock()

def initialize_screen() -> pygame.Surface:
    screen = pygame.display.set_mode((SCREEN_WIDTH_HEIGHT, SCREEN_WIDTH_HEIGHT))
    pygame.display.set_caption('N Queens')
    screen.fill((255, 255, 255))
    return screen


def main_gui():
    screen = initialize_screen()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255, 255, 255))
        pygame.display.update()