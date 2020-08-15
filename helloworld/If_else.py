house_price = int(input('How much is the price of house? '))
is_buyercredit = input('Is buyer credit good? [True/False] ').title()
down_payment = 100
if is_buyercredit:
    down_payment = 10
    print(f'down payment is {down_payment}%')
else:
    down_payment = 20
    print(f'down payment is {down_payment}%')

dp = house_price * down_payment /100
print(f'Please pay down payment of {down_payment}% amounting to SR {dp}')