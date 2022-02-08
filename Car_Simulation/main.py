choice = ''

while choice != 'QUIT':
    choice = input('')
    if choice.upper() == 'START':
        print("Car started. Ready to go!")
    elif choice.upper() == 'STOP':
        print('Car stopped')
    elif choice.upper() == 'QUIT':
        break
    else:
        print("I don't understand")
