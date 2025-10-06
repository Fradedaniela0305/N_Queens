import pygame

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_CORAL_ORANGE = (255,127,80)
COLOR_NEON_GREEN = (57, 255, 20)


SCREEN_WIDTH_HEIGHT = 800
NUMBER_FONT_SIZE = int(30 + SCREEN_WIDTH_HEIGHT*0.1)
TEXT_FONT_SIZE = 32
FONT = "data/font.ttf"

NUMBER_MESSAGE = "number"
NOT_A_NUMBER_MESSAGE = "not_a_number"
TOO_BIG_NUMBER = "too_big_number"




def verify_user_input(text_box):
    try:
        value = int(text_box)
    except ValueError:
        return NOT_A_NUMBER_MESSAGE

    if value >= 100:
        return TOO_BIG_NUMBER

    return NUMBER_MESSAGE

