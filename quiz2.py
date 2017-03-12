import random

def end():
    stop()

def askType():
    print ( 'Do you want to add, subtract, multiply, or divide (no decimals) ? Type in add, sub, mul, or div.')
    a = input()
    if a == 'div':
        division()
    print ('Do you want to work with a custom number, or have me choose a random one? Enter "1" to choose a number,or "2" to have me choose one.')
    c = input()
    if c == '1':
        print ( 'Enter a number to work with.')
        number1 = input()
        number1 = int(number1)
    elif c == '2':
        number1 = random.randint(1, 9)
    else:
        raise Exception('There was an error with your 2nd input. Please try again. ')
    print ('number is set to:', number1)
    return a, number1

def iteration():
    a, number1 = askType()
    while True:
        i = random.randint(1,9)
        if a == 'add':
            ans = i + number1
            b = '+'
        elif a == 'sub':
            ans = i - number1
            b = '-'
        elif a == 'mul':
            ans = i * number1
            b = 'x'
        elif a == 'div':
            ans = i / number1
            b = 'divided by'
        else:
            print('There was an error with your 1st input. Please try again.')
            return
        print("What's", i, b, number1, '?')
        guess = input()
        if guess == 'stop':
            print('s')
        if guess == 'skip':
            print ('Skipping')

        if guess == 'restart':
            print('Restarting...')
            return
        if int(guess) == ans:
            print('Correct!')
        else:
            print ("No, it's", ans)

def main():
    while True:
        try:
            r = iteration()
        except Exception as e:
            print (str(e))
            continue


def division():
    while True:
        number2 = random.randint(1,9)
        number3 = random.randint(1,9)
        number4 = number2 * number3
        f = random.randint(1,2)
        if f == 1:
            ans = number4 / number2
            print('Whats', number4, 'divided by', number2, '?')
        else:
            ans = number4 / number3
            print ('Whats', number4, 'divided by', number3, '?')
        guess = input()
        if guess == 'stop':
            end()
        if guess == 'skip':
            print ('Skipping')
            division()
        if guess == 'restart':
            print('Restarting...')
            askType()
        if guess == ans:
            print('Correct!')
        else:
            print("No, it's", ans)

def stop():
    print('Stopped')
main()