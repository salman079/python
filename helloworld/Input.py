name = input('what is your name? ')
eat = input('what do you want to eat? ')
birth_year = input('year of birth: ')
print('before calculation birth year has type ')
print(type(birth_year))
age = 2020 - int(birth_year)
print('after calculation birth year has type ')
print(type(birth_year))
print('Hi ' + name.title() + ' likes to eat ' + eat.title() + ' and has age of ' + str(age))
print(type(age))