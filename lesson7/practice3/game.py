import random
number = random.randint(1, 100)
guess = 0
while guess != number:
    guess = int(input('Guess a number: '))
    if guess == number:
        print('You win')
        break
    elif guess < number:
        print('Go higher')
    else:
        print('Go lower')