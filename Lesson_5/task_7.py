import json

with open('file_7.json', 'w+', encoding='UTF-8') as list:
    with open('file_7.txt', 'r', encoding='UTF-8') as firm:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in firm}
        average = [profit, {'Средняя прибыль': round(sum([int(i) for i in profit.values() if int(i) > 0])
            / len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(average, list, ensure_ascii=False, indent=7)
