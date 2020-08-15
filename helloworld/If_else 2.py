weight = int(input('Weight? '))
print (type(weight))
kg_lb = input('(L)bs or (K)g? ')

if kg_lb.lower() == 'l':
    converted = weight / 2.2
    print(f'converted to {converted} kg')
elif kg_lb.upper() == 'K':
    converted = weight * 2.2
    print(f'converted to {converted} lbs')
else:
    print('select correct option')