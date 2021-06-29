task = open('file_01.txt', 'w', encoding='utf-8')
while True:
    add_str = input('Enter value - ')
    if add_str == '':
        break
    task.write(add_str+'\n')
task.close()