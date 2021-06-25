my_list = [7, 3, 45, 13, 24, 5, 9, 61, 18]
high = [x for x in my_list if x > my_list[my_list.index(x)-1]]
print(high)