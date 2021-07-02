with open('file_03.txt', 'r', encoding='utf-8') as file:
    sal = []
    poor = []
    list = file.read().split('\n')
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')