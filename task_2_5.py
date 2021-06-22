base_list = [7, 5, 4, 4, 3, 3, 2]
user_number = int(input('Enter new rating item: '))
x = 0
for i in base_list:
    if user_number <= i:
        x += 1
    else:
        break
base_list.insert(x, user_number)
print(base_list)