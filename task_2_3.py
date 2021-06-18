season_list = ['Winter', 'Spring', 'Summer', 'Autumn']
season_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}

month_number = int(input('Enter month number: '))
if month_number == 1 or month_number == 12 or month_number == 2:
    print(season_list[0])
    print(season_dict.get(1))
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(season_list[3])
    print(season_dict.get(2))
else:
    print('Такого месяца не существует')

#seasons_list = [
    #['Winter', ['12', '1', '2']],
    #['Spring', ['3', '4', '5']],
    #['Summer', ['6', '7', '8']],
    #['Autumn', ['9', '10', '11']]
#]

#seasons_dict = {
    #'Winter': ['12', '1', '2'],
    #'Spring': ['3', '4', '5'],
    #'Summer': ['6', '7', '8'],
    #'Autumn': ['9', '10', '11']
#}

#while True:
    #month_number = input('Пожалуйста введите номер месяца: ')
    #if month_number not in sum(seasons_dict.values(), []):
        #print('Такого месяца не существует!')
        #continue

    #break

#for season, months in seasons_list:
    #if month_number in months:
        #print(f'Через список определено, что месяц с номером {month_number} это {season}')

#for season, months in seasons_dict.items():
    #if month_number in months:
        #print(f'Через словарь определено, что месяц с номером {month_number} это {season}')
