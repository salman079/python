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
fav_car = int(input("which car is your fav? [1-5] "))
fav_car-=1
print(f'My favaroite car is {cars[fav_car].title()}')
new_car=input("add a name of car in the list: ")
cars.append(new_car)
print(f"number of instance of {new_car} in list is {cars.count(new_car)}")
print(cars)
fruits99 = []
fruits99 = cars + ["apple", "banana"]
fruits99.insert(0,"Melon")
fruits99.insert(3,"grape")
print(fruits99)
print("grape is replaced with mango")
fruits99[3]="mango"
print(fruits99)
print(len(fruits99))
new_fruit=fruits99
fruits99.remove("toyota") # use value to remove
del fruits99[7]   # use index to remove
print(fruits99)
print(new_fruit)
fruits99.copy()
is_new = True
print(is_new)

a = "zindabad"
print(f"Pakistan {a.title()}")
fruits = ["mango", "cherry"]
print(fruits)
fruits.append('apple')
print(fruits)
dry_fruits = ["almod","kajo"]
print(dry_fruits)
fruits = fruits + dry_fruits
print(fruits)
fruits[4]="pistacho"
print(fruits)
fruits.insert(5,"kiwi")
print(fruits)
fruits.remove("kiwi")
print(fruits)
new_fruit=fruits.copy()
fruits.insert(0,"test")
print(fruits)
print(new_fruit)
fr=fruits
fruits.insert(0,"test")
print(fruits)
print(fr)
fruits.extend(["blue berry","black berry"])
print(fruits)
print(f'count test: {fruits.count("test")}')
print(f"len function: {len(fruits)}")
print(new_fruit)
new_fruit.clear()
print(new_fruit)
print(fruits)
print(f"index functionn {fruits.index('test')}") # return the index of first instance of the value
print (f"IN function {'test' in fruits}")  # to use in function
initial_fruits = fruits[:3]
endding_fruits = fruits[6:]
mid_fruits = fruits[2:7:2]
print(f"full list :{fruits}")
print(f"0-3: {initial_fruits}")
print(f"6-last: {endding_fruits}")
print(f"3-6: {mid_fruits}")
poped_fruits = []
print(fruits)
poped_fruits.extend([fruits.pop(5),fruits.pop(2)])
print(poped_fruits)
poped_fruits.insert(1,fruits.pop(4))
# poped_fruits = [initial_fruits.pop(1)+ mid_fruits.pop(1)+ endding_fruits(1)]
print(poped_fruits)
print(fruits)
fruits.reverse()
print(f"Reverse: {fruits}")
fruits.sort()
print(f"sort assending: {fruits}")
fruits.sort(reverse=True)
print(f"sort decending: {fruits}")
# Lists in list
l_l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"List in list: ",end="")
for a in l_l:
    for b in a:
        print(f" {b}",sep=' ', end='')
print("")
print(l_l[0][1])