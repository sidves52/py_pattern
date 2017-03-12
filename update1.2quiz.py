from random import randint

def customchoice():
    print('Do you want to customize your own settings(1), pick random settings(2), or pick everything random every q' +
    'uestion(default)?')
    choice1 = input()

    if choice1 == '1':
        print('Do you want to add(1), subtract(2), multiply(3), divide(4), pick random(5), or pick random settings e' +
        'very question(default)?')
        choice2 = input()
        if choice2 == 5:
            choice2 = randint(1, 4)
        print('Do you want to set a custom number to work with(1), pick something random to work with(2), or pick a ' +
        'random number every question(default)?')
        choice3 = input()
        if choice3 == '1':
            print('Enter the custom number.')
            setnumber = input()
            print('You are working with the number ', setnumber)
        elif choice3 == '2':
            setnumber = randint(1, 9)
            print('You are working with the number', setnumber)
        else:
            setnumber = 0
            print('You are working with the number ', setnumber)

    if choice1 == 2:
        choice2 = randint(1, 6)
        choice3 = randint(2, 3)
        if choice3 == 2:
            setnumber = randint(1, 9)
            print('You are working with the number ', setnumber)
        else:
            setnumber = 0

    else:
        choice2 = 0
        setnumber = 0
    return {'choice2': choice2,
            'setnumber': setnumber}

def mathcycle(config):
    choice2 = config['choice2']
    setnumber = config['setnumber']
    play = 1
    print(choice2)
    print(setnumber)
    if choice2 == 5:
        choice2 = randint(1, 4)
        pick_choice2 = True
    else:
        pick_choice2 = True
    if setnumber == 0:
        setnumberwrong = False
    if setnumber.isdigit():
        setnumberwrong = False
    if setnumberwrong != False:
        pick_setnumber = True
    while play == 1:
        if pick_choice2 == True:
            choice2 = randint(1, 4)
            if choice2 == 1:
                math_type = '+'
            elif choice2 == 2:
                math_type = '-'
            elif choice2 == 3:
                math_type = '*'
            elif choice2 == 4:
                math_type = 'divided by'
        if pick_setnumber == True:
            setnumber = randint(1, 9)
        setnumber2 = randint(1, 9)
        print('What is ', setnumber, math_type,setnumber2)
        guess = input()
        if math_type == '+':
            ans = setnumber + setnumber2
        elif math_type == '-':
            ans = setnumber - setnumber2
        elif math_type == '*':
            ans = setnumber * setnumber2
        elif math_type == 'divided by':
            ans = setnumber * setnumber2 / randint(1, 9)
        if guess == ans:
            print('Correct!')
        elif guess == 'stop':
            play += 1
        elif guess == 'restart':
            customchoice()
        elif guess == 'skip':
            mathcycle(config)
        else:
            print('Wrong, the answer was ', ans)
#eagercyclone33
def main():
    config = customchoice()
    mathcycle(config)

main()