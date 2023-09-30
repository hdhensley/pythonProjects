# Get the total change amount from the user
change = int(input())

if change < 1:
    print('No change')

# Calculate the number of Dollars
if change >= 100:
    # Use floor division to round down to the nearest integer
    dollars = change // 100
    # Singular
    if dollars == 1:
        print('1 Dollar')
    # Plural
    else:
        print('{} Dollars'.format(dollars))
    # Take the modulus of change and reassign it to pass down the remaining change
    change %= 100

# Calculate the number of Quarters
if change >= 25:
    # Use floor division to round down to the nearest integer
    quarters = change // 25
    # Singular
    if quarters == 1:
        print('1 Quarter')
    # Plural
    else:
        print('{} Quarters'.format(quarters))
    # Take the modulus of change and reassign it to pass down the remaining change
    change %= 25

# Calculate the number of Dimes
if change >= 10:
    # Use floor division to round down to the nearest integer
    dimes = change // 10
    # Singular
    if dimes == 1:
        print('1 Dime')
    # Plural
    else:
        print('{} Dimes'.format(dimes))
    # Take the modulus of change and reassign it to pass down the remaining change
    change %= 10

# Calculate the number of Nickels
if change >= 5:
    # Use floor division to round down to the nearest integer
    nickels = change // 5
    # Singular
    if nickels == 1:
        print('1 Nickel')
    # Plural
    else:
        print('{} Nickels'.format(nickels))
    # Take the modulus of change and reassign it to pass down the remaining change
    change %= 5

# Calculate the number of Pennies
if change >= 1:
    pennies = change
    # Singular
    if pennies == 1:
        print('1 Penny')
    # Plural
    else:
        print('{} Pennies'.format(pennies))
