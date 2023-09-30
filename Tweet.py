#symbols to be removed from tweets
symbols_to_remove = [",", ".", "!", "?"]

#used to check whether or not an abbreviation is found
abbreviation_found = False

# user input of upto 160 characters
tweet = input('Please enter your Tweet (max 160 characters): ')
if len(tweet) <= 160:
    for symbol in symbols_to_remove:
        tweet = tweet.replace(symbol, "")

    # split the Tweet into individual words.
    words = tweet.split()

    # if user input contains LOL
    if 'LOL' in words:
        # print laughing out loud
        print('LOL = laughing out loud')
        #change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains BFN
    if 'BFN' in words:
        # print bye for now
        print('BFN = bye for now')
        # change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains FTW
    if 'FTW' in words:
        # print for the win
        print('FTW = for the win')
        # change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains IRL
    if 'IRL' in words:
        # print in real life
        print('IRL = in real life')
        # change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains BRB
    if 'BRB' in words:
        # print Laugh out Loud
        print('BRB = be right back')
        # change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains G2G
    if 'G2G' in words:
        # print got to go
        print('G2G = got to go')
        # change abbreviation_found state to true
        abbreviation_found = True
    # if user input contains no abbreviations
    if not abbreviation_found:
        # print Sorry, don't know that one
        print("Sorry, don't know that one")
# if user input is too long
else:
    print('Your input exceeds 160 characters. Please enter a shorter string.')
