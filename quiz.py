import random

GO = 1
IS_RANDOM = False
MAX_VALUE = 5
FIRST_TIME = True

def printSuccess():
    i = random.randint(1, 1)
    if i == 1:
        print('Correct! Yay!')
        return
    if i == 2:
        print('Great Job!')
        return
    if i == 3:
        print('Congratulations!!!')
        return
    if i == 4:
        print('Awesome!!!!!')
        return
    if i == 5:
        print('Wow! Right again!')
        return

def askType():
    global IS_RANDOM
    global FIRST_TIME

    if FIRST_TIME:
        a = 'add'
        c = '2'
    else:
        print ( 'Do you want to add, subtract, multiply, or divide (no decimals) ? Type in add, sub, mul, or div.')
        a = input()

        print ('Do you want to work with a custom number, or have me choose a random one? Enter "1" to choose a number,or "2" to have me choose one.')
        c = input()

    if c == '1':
        print ( 'Enter a number to work with.')
        number1 = input()
        number1 = int(number1)
        print('number is set to:', number1)
    elif c == '2':
        IS_RANDOM = True
        number1 = random.randint(1, MAX_VALUE)
    else:
        raise Exception('There was an error with your 2nd input. Please try again. ')
    FIRST_TIME = False
    return a, number1

def iteration():
    a, number1 = askType()
    if a == 'div':
        return division(number1)
    while True:
        if IS_RANDOM:
            number1 = random.randint(1, MAX_VALUE)
        i = random.randint(1, MAX_VALUE)
        if a == 'add':
            ans = i + number1
            b = '+'
        elif a == 'sub':
            ans = i - number1
            b = '-'
        elif a == 'mul':
            ans = i * number1
            b = 'x'
        else:
            print('There was an error with your 1st input. Please try again.')
            return
        print("What's", i, b, number1, '?')
        guess = input()
        if guess == 'stop':
            stop()
            return
        if guess == 'skip':
            print ('Skipping')
            continue
        if guess == 'restart':
            print('Restarting...')
            return
        if int(guess) == ans:
            printSuccess()
        else:
            print ("No, it's", ans)

def main():
    global GO
    while GO == 1:
        try:
            r = iteration()
        except Exception as e:
            print (str(e))
            continue


def division(number1):
    while True:
        number2 = random.randint(1, MAX_VALUE)
        number3 = number1 * number2
        ans = int(number3 / number2)
        print('Whats', number3, 'divided by', number1, '?')
        guess = input()
        if guess == 'stop':
            stop()
            return
        if guess == 'skip':
            print ('Skipping')
            continue
        if guess == 'restart':
            print('Restarting...')
            askType()
        if guess == ans:
            print('Correct!')
        else:
            print("No, it's", ans)

def stop():
    global GO
    print('Stopped')
    GO = 2

main()