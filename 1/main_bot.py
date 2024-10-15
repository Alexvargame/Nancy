import pygame

#import config as c
from game_object import GameObject

class MainBot(GameObject):
    def __init__(self, x_pos, y_pos, image, dialog_dict=None):
        GameObject.__init__(self, x_pos, y_pos, image)

        self.rect = pygame.image.load(self.image).convert_alpha().get_rect(center=(x_pos, y_pos))
        self.obj = pygame.image.load(self.image).convert_alpha()
        self.dict = dialog_dict

    def draw(self, surface):
        pygame.draw.rect(surface)

    def info(self, text, x, y):
        self.obj.blit(text, (x, y))

    def speak(self, font, text, antialias, color):
        return font.render(text, antialias, color)

