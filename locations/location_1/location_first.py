

def print_coord():
    print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDddd')
    #grid_info = event.widget.grid_info()
    #self.tool_segment_2_lbl.config(text=f'{grid_info["column"]}:{grid_info["row"]}')
THE_BACKGROUND = 'images/355.png'
THE_OBJECTS ={
  'THE_BOT': {
      'main_bot':{
          'location':(24,7),
          'width':5,
          'height':6,
          'name':'MAIN_BOT',
          'state': 'normal',
      },
          'a_bot': {
              'location': (1, 1),
              'width': 2,
              'height': 2,
              'name': 'A_BOT',
              'state': 'normal',
          },
  },
  'THE_FURNITURE': {
      'key_safe':{
          'location':(5,5),
          'width':3,
          'height':3,
          'name':'KAY_SAFE',
          'state': 'normal',
      }
  }
}

THE_DIALOGS ={

  'PLAYER_DIALOG' :{
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
                  }
              }
          },
      'a_bot':
          {
              'state': {
                  1: {
                      'text': 'Привет!',
                      'act': 0
                  },
                  2: {
                      'text': 'Не запылись',
                      'act': 0
                  }
              }
          },
      'door': {
          'location': (17, 1),
          'width': 3,
          'height': 10,
          'name': 'DOOR',
          'state': 'disabled',
          },
  },

  'MAIN_BOT_DIALOG' :{
    'state': {
                1:{
                    'text':['Привет, искатель'],
                    'act':0
                },
                2:{
                    'text':['Поищи в ящике','KEY_SAFE_DIALOG'],
                    'act':1
                }
        }
    },
'A_BOT_DIALOG' :{
    'state': {
        1:{
            'text':['Привет, я тут для мебели'],
            'act':1
        },
    }
    },
  'KEY_SAFE_DIALOG': {
    'name': 'SAFE',
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
