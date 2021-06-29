name = input('Enter name: ')
surname = input('Enter surname: ')
year_born = input('Enter year born: ')
city = input('Enter city: ')
email = input('Enter email: ')
telephone = input('Enter telephone number: ')


def my_func(name, surname, year_born, city, email, telephone):
    return ' '.join([name, surname, year_born, city, email, telephone])


print(my_func(name, surname, year_born, city, email, telephone))