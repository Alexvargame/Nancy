import pygame
from sys import exit

from locations.location_1.loc_objects import OBJECTS_DICT, BACKGROUND_IMAGE


def game():
    pygame.init()

    width = 1000
    height = 620
    fps = 60

    clock = pygame.time.Clock()
    main_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Nancy')

    RECT_DICT = {}

    width_dialog_window = 1000
    height_dialog_window = 100
    dialog_window = pygame.Surface((width_dialog_window, height_dialog_window))
    dialog_window_font = pygame.font.Font('fonts/prstartk.ttf', 10)
    dialog_window_text = dialog_window_font.render('HELLO', False, 'Red')
    dialog_window.fill('White')

    background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
    for key, value in OBJECTS_DICT.items():
        RECT_DICT[key] = {'obj': '',
                          'rect': ''}
        tmp = pygame.image.load(value['image']).convert_alpha()
        RECT_DICT[key]['obj'] = tmp
        RECT_DICT[key]['rect'] = tmp.get_rect(center=(value['x_pos'], value['y_pos']))
    game = True
    #doMove = False
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        main_screen.blit(background, (0, 0))

        for key, value in RECT_DICT.items():
            main_screen.blit(RECT_DICT[key]['obj'], RECT_DICT[key]['rect'])

        main_screen.blit(dialog_window, (0, 540))
        dialog_window.blit(dialog_window_text, (400, 50))
        keys = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for key, value in RECT_DICT.items():
                print(value)
                if pygame.Rect.collidepoint(value['rect'], x, y):
                    if event.button == 1:
                        print(key)
                    elif event.button == 3:
                        txt = dialog_window_font.render(f'This is {key}', False, 'Red')
                        value['obj'].blit(txt, (0, 0))#(OBJECTS_DICT[key]['x_pos'],OBJECTS_DICT[key]['y_pos']))

        pygame.display.update()
        clock.tick(fps)





def main():
    game()

if __name__ == '__main__':
    main()
