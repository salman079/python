msg = """
Start = to start the car
Stop = to stop the car
Quit = to quit from the game
Help = to print options"""
print(msg)
option = ""
started = False
while True:
    option = input('> ').lower()
    if option == 'start':
        if started:
            print ('car is already started')
        else:
            started = True
            print('car is started')
    elif option == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('car is stopped')
    elif option == 'help':
        print(msg)
    elif option == 'quit':
        break
    else:
        print('give the correct command!!!!')
print('Game finished bye !!!!!!')