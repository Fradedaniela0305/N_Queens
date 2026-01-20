import pygame, sys
from utils import *
from GUI import main_gui

pygame.init()
clock = pygame.time.Clock()
BASE_NUMBER_FONT = pygame.font.Font(FONT, NUMBER_FONT_SIZE)
BASE_TEXT_FONT = pygame.font.Font(FONT, TEXT_FONT_SIZE)



def main_menu():
    user_text = ''
    text_box_width = NUMBER_FONT_SIZE * 3
    active = False
    color = (0, 0, 0)
    screen = initialize_screen("Welcome to N-Queens!")
    text_box = pygame.Rect(((SCREEN_WIDTH_HEIGHT / 2) - (text_box_width / 2), SCREEN_WIDTH_HEIGHT / 2),
                           (text_box_width, NUMBER_FONT_SIZE))

    error_box_length = 18*TEXT_FONT_SIZE

    error_box = pygame.Rect((SCREEN_WIDTH_HEIGHT / 2 - error_box_length/2,300), (error_box_length, TEXT_FONT_SIZE))



    while True:

        pygame.draw.rect(screen, color, text_box, 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                        # text_box_width = text_box_width + max(0, (len(user_text) -2)*NUMBER_FONT_SIZE)
                        # TODO
                    else:
                        user_text += event.unicode
                        # text_box_width = text_box_width + max(0, (len(user_text) - 2) * NUMBER_FONT_SIZE)
                        # TODO

                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    message = verify_user_input(user_text)

                    if message == NUMBER_MESSAGE:
                        main_gui(int(user_text))
                    elif message == NOT_A_NUMBER_MESSAGE:
                        display_error_message(screen, 'ENTER A VALID NUMBER', error_box, text_box)
                        user_text = ''



                    elif message == TOO_BIG_NUMBER:
                        display_error_message(screen, "YOU'LL CRASH", error_box, text_box)
                        user_text = ''



        if active:
            color = (57, 255, 20)
        else:
            color = (255,127,80)

        screen.fill((2, 12, 102), text_box)
        pygame.draw.rect(screen, color, text_box, 2)
        text = BASE_NUMBER_FONT.render(user_text, True, color)
        screen.blit(text, text_box)
        pygame.display.update()


        # pygame.draw.rect(screen, color, text_box, 2)
        # text = BASE_NUMBER_FONT.render(user_text, True, color)
        # screen.blit(text, text_box)
        # pygame.display.update()


def display_error_message(screen, message, error_box, text_box):
    fail_text = BASE_TEXT_FONT.render("ENTER VALID NUMBER", True, (255, 0, 0))
    fail_text_rect = fail_text.get_rect(center=error_box.center)
    screen.blit(fail_text, fail_text_rect)
    pygame.display.update()
    pygame.time.wait(1000)
    screen.fill((2, 12, 102), error_box)
    screen.fill((2, 12, 102), text_box)


def initialize_screen(title):
    screen = pygame.display.set_mode((SCREEN_WIDTH_HEIGHT, SCREEN_WIDTH_HEIGHT))
    screen.fill((2, 12, 102))
    render_text_image(screen, title, COLOR_WHITE, (100,100))
    render_text_image(screen, "Enter number of queens", COLOR_WHITE, (70, 200))
    return screen

def render_text_image(screen, text, color, position):
    text_image = BASE_TEXT_FONT.render(text, True, color)
    screen.blit(text_image, position)

