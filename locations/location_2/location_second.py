

def print_coord():
    print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDddd')


THE_BACKGROUND = 'images/1588.png'
THE_NEXT_LOCATION = 'locations.location_3'
THE_OBJECTS = {
  'THE_BOT': {
      'main_bot': {
          'location': (20, 14),
          'width': 3,
          'height': 6,
          'name': 'MAIN_BOT',
          'state': 'normal',
      },
      'cat': {
          'location': (10, 26),
          'width': 1,
          'height': 2,
          'name': 'CAT',
          'state': 'normal',
      }

  },
  'THE_FURNITURE': {
      'door': {
          'location': (17, 1),
          'width': 3,
          'height': 10,
          'name': 'DOOR',
          'state': 'disabled',
      },
      'key_safe': {
          'location': (8, 7),
          'width': 3,
          'height': 7,
          'name': 'KEY_SAFE',
          'state': 'normal',
      },
      'table': {
          'location': (0, 29),
          'width': 30,
          'height': 1,
          'name': 'TABLE',
          'state': 'normal',
      },

      'shelf': {
          'location': (29, 6),
          'width': 1,
          'height': 1,
          'name': 'SHELF',
          'state': 'normal',
      },

  }
}

THE_DIALOGS = {

  'PLAYER_DIALOG': {
      'main_bot':
          {
              'state': {
                  1: {
                      'text': 'Привет',
                      'act': 0
                  },
                  2: {
                      'text': 'Мне нужен ключ',
                      'act': 0
                  },
                  3: {
                      'text': '',
                      'act': 0
                  }
              }
          },
      'cat':
          {
              'state': {
                  1: {
                      'text': 'Ух-ты, кот',
                      'act': 0
                  },
                  2: {
                          'text': '))',
                          'act': 0
                      },
                  }
          },
          'door':
          {
              'state': {
                  1: {
                      'text': 'Я ушел',
                      'act': 1
                  },
                  }
          }
    },

  'MAIN_BOT_DIALOG': {
    'state': {
        1: {
            'text': ['Привет, искатель'],
            'act': 0
        },
        2: {
            'text': ['Возьми книгу и запиши свое имя', 'TABLE_DIALOG'],
            'act': 1
        },
        3: {
            'text': ['Поищи в ящике', 'KEY_SAFE_DIALOG'],
            'act': 1
        }
        }
        },
    'CAT_DIALOG': {
        'state': {
            1: {
                'text': ['Мур'],
                'act': 0
            },
        }
        },
    'SHELF_DIALOG': {
        'state': {
            0: {
                'text': ['Книги'],
                'act': 0
            },
        }
        },
    'KEY_SAFE_DIALOG': {
        'name': 'SAFE',
        'action': 'Key',
        'state': {
          0: {
            'text': 'У меня для тебя ничего нет',
            'act': 0
          },
          1: {
            'text': 'Вот твой ключ',
            'act': 0
          }
        }
        },
    'TABLE_DIALOG': {
        'name': 'TABLE',
        'state': {
          0: {
            'text': 'Просто стол',
            'act': 0
          },
          1: {
            'text': 'Хорошо',
            'act': 1
          },
        }
      },
    'DOOR_DIALOG': {
        'name': 'DOOR',
        'de_action': 'Key',
        'state': {
          0: {
            'text': 'Закрыто',
            'act': 0
          },
          1: {
            'text': 'До встречи',
            'act': 1
          },
        }
      }
    }
