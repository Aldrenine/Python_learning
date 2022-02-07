weight = input("Weight: ")

scale = input("(L)bs or (K)g: ")

if scale.upper() == 'L':
    con = float(weight) / 2.205
    print("you are " + str(con) + " kgs.")
elif scale.upper() == 'K':
    con = int(weight) * 2.205
    print(f'you are {con} lbs')
else:
    print('Not a valid option')
