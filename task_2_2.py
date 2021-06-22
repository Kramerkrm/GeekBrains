user_list = list(input('Введите символы без пробела - '))
print('Ваш список: ', user_list)

change = len(user_list) if len(user_list) % 2 == 0 else len(user_list) - 1

user_list[:change:2], user_list[1:change:2] = user_list[1:change:2], user_list[:change:2]
print('Измененный список: ', user_list)