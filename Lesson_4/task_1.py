from sys import argv

def zp():
    try:
        hours, rate, prem = map(float, argv[1:])
        print(f'Вы думаетее это- {hours * rate + prem} хорошая зарплата?')
    except ValueError:
        print('Введите правильные значения!')


zp()