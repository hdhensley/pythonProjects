import random

astrix = ''
dice_rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
        print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))

        dice_rolls[roll_total] += 1

    print('\nDice roll histogram:')
    for i in range(2, 13):
        print('{}s: {}'.format(i, '*' * dice_rolls[i]))
else:
    print('Invalid number of rolls. Try again.')
