    back = pygame.image.load('images/back_null_location.png').convert_alpha()
    #main_bot = pygame.image.load('images/main_bot.png').convert_alpha()
    key_safe = pygame.image.load('images/key_safe.png').convert_alpha()
    shelf = pygame.image.load('images/shelf.png').convert_alpha()
    door = pygame.image.load('images/door.png').convert_alpha()
    cat = pygame.image.load('images/cat.png').convert_alpha()
    table = pygame.image.load('images/table.png').convert_alpha()

    # main_bot_x_pos = 718
    # main_bot_y_pos = 316
    # key_safe_x_pos = 260
    # key_safe_y_pos = 260
    # shelf_x_pos = 970
    # shelf_y_pos = 135
    # door_x_pos = 580
    # door_y_pos = 139
    # cat_x_pos = 300
    # cat_y_pos = 445
    # table_x_pos = 576
    # table_y_pos = 510

    # main_bot_rect = main_bot.get_rect(center=(main_bot_x_pos, main_bot_y_pos))
    # key_safe_rect = key_safe.get_rect(center=(key_safe_x_pos, key_safe_y_pos))
    # shelf_rect = shelf.get_rect(center=(shelf_x_pos, shelf_y_pos))
    # door_rect = door.get_rect(center=(door_x_pos, door_y_pos))
    # table_rect = table.get_rect(center=(table_x_pos, table_y_pos))
    # cat_rect = cat.get_rect(center=(cat_x_pos, cat_y_pos))

# main_screen.blit(table, table_rect)
# main_screen.blit(main_bot, main_bot_rect)
# main_screen.blit(key_safe, key_safe_rect)
# main_screen.blit(shelf, shelf_rect)
# main_screen.blit(door, door_rect)
# main_screen.blit(cat, cat_rect

# class GameObject:
#     def __init__(self, x, y, w, h, speed=(0,0)):
#         self.bounds = Rect(x, y, w, h)
#         self.speed = speed
#
#     @property
#     def left(self):
#         return self.bounds.left
#
#     @property
#     def right(self):
#         return self.bounds.right
#
#     @property
#     def top(self):
#         return self.bounds.top
#
#     @property
#     def bottom(self):
#         return self.bounds.bottom
#
#     @property
#     def width(self):
#         return self.bounds.width
#
#     @property
#     def height(self):
#         return self.bounds.height
#
#     @property
#     def center(self):
#         return self.bounds.center
#
#     @property
#     def centerx(self):
#         return self.bounds.centerx
#
#     @property
#     def centery(self):
#         return self.bounds.centery
#
#     def draw(self, surface):
#         pass
#
#     def move(self, dx, dy):
#         self.bounds = self.bounds.move(dx, dy)
#
#     def update(self):
#         if self.speed == [0, 0]:
#             return
#
#         self.move(*self.speed)

    #     obj_dict[key] = {'obj': '',
    #                      'rect': ''}
    #     tmp = pygame.image.load(value['image']).convert_alpha()
    #     obj_dict[key]['obj'] = tmp
    #     obj_dict[key]['rect'] = tmp.get_rect(center=(value['x_pos'], value['y_pos']))