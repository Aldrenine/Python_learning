import random

answer = random.randint(1, 10)

tries = 0

while tries < 3:
    tries = tries + 1
    guess = input('Guess a number from 1 to 10: ')
    if int(guess) == answer:
        print('Correct')
        break
    elif int(guess) > 10 or int(guess) < 1:
        print('Guess out for range!')
    else:
        print('Incorrect')

print(answer)
