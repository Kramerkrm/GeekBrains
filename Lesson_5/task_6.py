object = {}
with open('file_6.txt', 'r', encoding='UTF-8') as file:
    for study in file:
        study = study.replace(':', '').replace('—', '0').replace('(л)', '').replace('(пр)', '').replace('лаб', '').replace('()', '').split()
        object[study[0]] = sum(map(int, study[1:]))
print(f'Сумма часов по предметам - \n{object}')
