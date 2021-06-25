num_int = int(input('Введите целое положительное число: '))
maximum_dig = 0
num = num_int

while num > 0:
    digit = num % 10
    if digit > maximum_dig:
        maximum_dig = digit
        if maximum_dig == 9:
            break
    num = num // 10

print(f'Наибольшая цифра в числе {num_int} это {maximum_dig}')