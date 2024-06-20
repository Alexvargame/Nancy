

THE_BACKGROUND = 'images/355.png'
THE_NEXT_LOCATION = ''

THE_OBJECTS ={
  'THE_BOT': {
      'main_bot':{
          'location':(24,7),
          'width':5,
          'height':6,
          'name':'MAIN_BOT',
          'state': 'disabled',
      },
      'a_bot': {
              'location': (1, 1),
              'width': 2,
              'height': 2,
              'name': 'A_BOT',
              'state': 'disabled',
          },
  },
  'THE_FURNITURE': {
      'key_safe':{
          'location':(5,5),
          'width':3,
          'height':3,
          'name':'KAY_SAFE',
          'state': 'disabled',
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
          }
    },

  'MAIN_BOT_DIALOG' :{
    'state':{
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
    'state':{
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
  }
}
