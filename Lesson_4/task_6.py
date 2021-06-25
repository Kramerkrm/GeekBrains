from itertools import count, cycle

number = count(17)
string = cycle('ZXC')

for el in range(10):
    print('(number:string) = ({}:{})'.format(next(number), next(string)))