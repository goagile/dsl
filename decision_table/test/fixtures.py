pznt = {
    'from_file': {
        'ПЗНТ': {
            '1 stage': {
                'Время несрабатывания': {
                    'Входы': {
                        'x': 'Xmax',
                        'y': 'Ycur'
                    },
                    'Выходы': {
                        'z':   '/Block1/1 st./Zmax',
                        'dis': '/Block1/1 st./disable'
                    },
                    'Условия': [
                        ['!None', '>0', 'y',   '0'],
                        ['None',  '0',  'y+8', '1']
                    ]
                }
            }
        }
    },

    'case_1': {
        'parsed_settings': {
            'ПЗНТ': {
                '1 stage': {
                    'Время не срабатывания': {
                        'Xmax': 3,
                        'Ycur': 2
                    }
                }
            }
        },
        'to_bf': {
            '/Block1/1 st./Zmax': 2,
            '/Block1/1 st./disable': 0
        }
    },

}
