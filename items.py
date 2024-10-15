from player import Player

class Key():
    def __init__(self, name, player, description=''):
        self.name = name
        self.player = player
        self.description = description

    def __str__(self):
        return self.name