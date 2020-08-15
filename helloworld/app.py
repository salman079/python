print("Hassan")
course_1 = "Python's course for Beginners"
course_2 = 'Python for "Beginners"'
print(course_1)
print(course_2)
# Listing
print('-' * 10)
print("List")
print('-' * 10)
cars = ['toyota','honda','audi','cherverlet','bmw']
print(cars)
srn = 0
print('SR# Car Name')
for car in cars:
    srn = srn + 1
    print(f'{srn} - {car.title()}')
print('-' * 50)
print(f'My favaroite car is {cars[4].title()}')
is_new = True
print(is_new)
