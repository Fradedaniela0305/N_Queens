# GUI.py
import sys
import pygame
from n_queens import n_queens


SCREEN_WIDTH_HEIGHT = 800


def initialize_screen() -> pygame.Surface:
    screen = pygame.display.set_mode((SCREEN_WIDTH_HEIGHT, SCREEN_WIDTH_HEIGHT))
    pygame.display.set_caption('N Queens')
    screen.fill((255, 255, 255))
    return screen


def main_gui(n):
    screen = initialize_screen()

    squares_coordinates = display_board(screen, n)

    resulting_squares = n_queens(n)

    display_queens(screen, squares_coordinates,resulting_squares, n)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def display_board(screen, n) -> list:
    square_length = (SCREEN_WIDTH_HEIGHT-100)/n
    dark_brown_square = get_dark_brown_square(square_length)
    light_brown_square = get_light_brown_square(square_length)

    points = []

    for i in range(n):
        for j in range(n):
            x, y = 50 + square_length * j, 50 + square_length * i
            points.append((x,y))

            if (i + j) % 2 == 0:
                screen.blit(dark_brown_square, (x, y))
            else:
                screen.blit(light_brown_square, (x, y))

    pygame.display.update()

    return points

def display_queens(screen, squares_coordinates, results, n):
    if not results: # TODO
        return False

    queen_image = get_queen_image(n)
    square_length = (SCREEN_WIDTH_HEIGHT - 100) / n

    for result in results:
        position = squares_coordinates[result - 1]
        x, y = position
        my_rect = pygame.Rect(x, y, square_length, square_length)

        queen_image_rect = queen_image.get_rect()
        queen_image_rect.center = my_rect.center

        screen.blit(queen_image, queen_image_rect)

def get_queen_image(n):

    square_length = (SCREEN_WIDTH_HEIGHT-100)/n
    queen_size = square_length - square_length*0.2
    queen_image = pygame.image.load("images/queen_image.png")
    resized_image = pygame.transform.scale(queen_image, (queen_size, queen_size))
    return resized_image

def get_dark_brown_square(square_length):
    # Return dark brown square image
    dark_brown_square = pygame.image.load("images/dark_brown_square.png")
    resized_image = pygame.transform.scale(dark_brown_square, (square_length, square_length))
    return resized_image

def get_light_brown_square(square_length):
    # Return light brown square image
    light_brown_square = pygame.image.load("images/light_brown_square.png")
    resized_image = pygame.transform.scale(light_brown_square, (square_length, square_length))
    return resized_image