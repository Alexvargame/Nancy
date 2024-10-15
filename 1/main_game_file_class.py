import pygame
import importlib
from sys import exit

from collections import defaultdict

import config as c
#from locations.location_1.loc_objects import OBJECTS_DICT, BACKGROUND_IMAGE

from main_bot import MainBot
from objects_bot import ObjectBot

class Nancy:

    def __init__(self, caption, width, height, frame_rate):
        self.caption = caption
        self.width = width
        self.heigth = height
        self.fps = frame_rate
        self.game_over = False
        self.objects = []
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.main_screen = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption(caption)
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    # def update(self):
    #     for o in self.objects:
    #         o.update()
    #
    # def draw(self):
    #     for o in self.objects:
    #         o.draw(self.surface)
    def game(self, loc='locations.location_1'):
        location = importlib.import_module(loc)
        #pygame.init()

        print(location.THE_DIALOGS)
        RECT_DICT = {}

        width_dialog_window = 1000
        height_dialog_window = 100
        dialog_window = pygame.Surface((width_dialog_window, height_dialog_window))
        dialog_window_font = pygame.font.Font('fonts/prstartk.ttf', 10)
        dialog_window_text = dialog_window_font.render('HELLO', False, 'Red')

        dialog_window.fill('White')
        dialog_window.blit(dialog_window_text, (400, 50))
        background = pygame.image.load(location.BACKGROUND_IMAGE).convert_alpha()
        RECT_DICT = self.set_objects(location.OBJECTS_DICT, location)
        game = True
        #doMove = False
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.main_screen.blit(background, (0, 0))
            for key, value in RECT_DICT.items():
                self.main_screen.blit(value.obj, value.rect)
            self.main_screen.blit(dialog_window, (0, 540))


            keys = pygame.mouse.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for key, value in RECT_DICT.items():
                    if pygame.Rect.collidepoint(value.rect, x, y):
                        if event.button == 1:
                            print(value.dict['state'][1]['text'])
                            dialog_window.fill('White') ##################################################??????
                            dialog_window.blit(value.speak(dialog_window_font, value.dict['state'][1]['text'][0], False, 'Red'), (400, 50))
                            # dialog_window.blit(dialog_window_font.render(value.dict['state'][1]['text'][0], False, 'Red'), (400, 50))
                        elif event.button == 3:

                            txt = dialog_window_font.render(f'This is {key}', False, 'Red')
                            value.info(txt, 0, 0)#(OBJECTS_DICT[key]['x_pos'],OBJECTS_DICT[key]['y_pos']))
            pygame.display.update()
            self.clock.tick(self.fps)

    def set_objects(self, adict, location):
        obj_dict = {}
        for key, value in adict.items():
            if key == 'main_bot':
                tmp_key = key.upper()+'_DIALOG'
                tmp_dict = location.THE_DIALOGS[tmp_key]
                obj_dict[key] = MainBot(value['x_pos'], value['y_pos'], value['image'], location.THE_DIALOGS[tmp_key])
            else:
                tmp_key = key.upper() + '_DIALOG'
                obj_dict[key] = ObjectBot(value['x_pos'], value['y_pos'], value['image'], location.THE_DIALOGS[tmp_key])

        return obj_dict





def main():
    N = Nancy(c.caption, c.width, c.height, c.frame_rate)
    N.game()

if __name__ == '__main__':
    main()
