guess = 0
loop = 0
# while loop < 3:
while True:
    loop = loop+1
    print(f"guess # {loop}")
    guess = int(input('Guess: '))
    if guess == 9:
        print("correct guess")
        break
    else:
        print('wrong guess')
else:
    print('Failed')
print('Game Finished')
