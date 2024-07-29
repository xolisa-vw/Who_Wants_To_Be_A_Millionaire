# code for Who wants To Be A Millionaire project

while True:
    print('\nThis is a game - "Who Wants To Be A Millionaire"')
    print('What is your name?')
    name = input('Name: ')

    print('\nWelcome to the game, ' + name)
    print('\nSo, the first question for R5000')

    bank = 0

    print('\nWhat is the capital of South Africa?')
    print('Answer options: ')
    print('A, Johannesburg')
    print('B, Cape Town')
    print('C, Pretoria')
    print('D, East London')

    answer = input('\nYour answer - ')

    if answer == 'C' or answer == 'c':
        print('Correct!')
        bank += 5000
        print('Your bank is: ' + str(bank))
    else:
        print('That answer is INCORRECT!')
        print('Your game is over')
        print('Your bank is: ' + str(bank))
        break

    print('\nSo, the second question for R10000')

    print('\nWhat social application is Mark Zuckerberg famous for?')
    print('Answer options: ')
    print('A, Twitter')
    print('B, Facebook')
    print('C, Instagram')
    print('D, SnapChat')

    answer = input('\nYour answer - ')

    if answer == 'B' or answer == 'b':
        print('Correct!')
        bank += 10000
        print('Your bank is: ' + str(bank))
    else:
        print('That answer is INCORRECT!')
        print('Your game is over')
        print('Your bank is: ' + str(bank))
        break
    
    print('\nSo, the third question for R50000')

    print('\nIn Formula One, which driver has recorded the most wins in the sports history?')
    print('Answer options: ')
    print('A, Michael Schumacher')
    print('B, Ayrton senna')
    print('C, Nicki Lauder')
    print('D, Lewis Hamilton')

    answer = input('\nYour answer - ')

    if answer == 'D' or answer == 'd':
        print('Correct!')
        bank += 50000
        print('Your bank is: ' + str(bank))
    else:
        print('That answer is INCORRECT!')
        print('Your game is over')
        print('Your bank is: ' + str(bank))
        break

    print('\nSo, the fourth question for R100000')

    print('\nWhat is the strongest muscle in the human body?')
    print('Answer options: ')
    print('A, Jaw Muscle (Masseter)')
    print('B, Quadricep')
    print('C, Tongue')
    print('D, Heart')

    answer = input('\nYour answer - ')

    if answer == 'A' or answer == 'a':
        print('Correct!')
        bank += 100000
        print('Your bank is: ' + str(bank))
    else:
        print('That answer is INCORRECT!')
        print('Your game is over')
        print('Your bank is: ' + str(bank))
        break
    print('\nThe fifth and final question for R500000')

    print('\nIn 2020, South Africa recorded its first Covid-19 case. What country was the citizen travelling from?')
    print('Answer options: ')
    print('A, France')
    print('B, Italy')
    print('C, USA')
    print('D, Australia')

    answer = input('\nYour answer - ')

    if answer == 'B' or answer == 'b':
        print('Correct!')
        bank += 500000
        print('Your bank is: ' + str(bank))
        print('CONGRATULATIONS! You won the game!')
    else:
        print('That answer is INCORRECT!')
        print('Your game is over')
        print('Your bank is: ' + str(bank))
        break

  