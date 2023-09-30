input_month = input()
input_day = int(input())

# Check for valid date
valid_date = True
if input_month in ['January', 'March', 'May', 'July', 'August', 'October', 'December'] and (
        input_day < 1 or input_day > 31):
    valid_date = False
elif input_month in ['April', 'June', 'September', 'November'] and (input_day < 1 or input_day > 30):
    valid_date = False
elif input_month == 'February' and (
        input_day < 1 or input_day > 29):  # Simplified check; ideally we should determine leap years
    valid_date = False

# If the date is not valid, print an error message and exit
if not valid_date:
    print('Invalid')
else:
    # Determine the season
    if (input_month == 'March' and input_day >= 20) or (input_month == 'April' or input_month == 'May') or (
            input_month == 'June' and input_day <= 20):
        season = 'Spring'
    elif (input_month == 'June' and input_day >= 21) or (input_month == 'July' or input_month == 'August') or (
            input_month == 'September' and input_day <= 21):
        season = 'Summer'
    elif (input_month == 'September' and input_day >= 22) or (
            input_month == 'October' or input_month == 'November') or (input_month == 'December' and input_day <= 20):
        season = 'Autumn'
    elif (input_month == 'December' and input_day >= 21) or (input_month == 'January' or input_month == 'February') or (
            input_month == 'March' and input_day <= 19):
        season = 'Winter'
    else:
        season = 'Invalid'

    # Print the season
    print(season)