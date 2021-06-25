n = input('Enter an integer: ')

while n < '0':
    print('Please try again! The number must be greater than 0')
    n = input('Enter number greater than 0:')

print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n)  + int(n + n + n)}')

