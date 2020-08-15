e = [6,2,2,6,2,2,6]
f = [6,2,2,6,2,2,2]
i = 0
for i in e:
    print(f'*' * i)
j = 0
a = 0
for j in f:
    p = ''
    for a in range(j):
        p=p+'x'
    print(p)

numbers = [5,85,215,6,8,54,55,2,9,69,311]
print (numbers)
print (f"total number of components in numbers using len() function {len(numbers)}")
# print (f"total number of components in numbers using len() function {range(numbers)}")
max = 0
for number in numbers:
   if max < number:
       max = number
print (f"maximum number in the list is {max}")