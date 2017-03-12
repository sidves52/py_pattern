import turtle
from random import randint
from misc import say

def keepdrawing():
    go = 1
    while go == 1:
        stop = input()
        if stop == 'stop':
            go += 1

def choices():
    say('Pick a number between 1 & 16, or type "skip"', voice = 'Pipe organ', rate = 260)
    skip = input()
    if skip == 'skip':
        pic = 'abc'
    say('Type "0" if you want to repeat, and "00" if you want the complete list.')
    left = 0
    pic = input()
    if pic == 'skip':
        pic = input()
    if pic == '00':
        say('(1)Cone, (2)illusion, (3)second illusion, (4)third illusion, (5)spiral, (6)six sided spiral, (7)hexagonbal'
        'l, (8)illuminati, (9)pyramid, (10)fans, (11)ninecorners, (12)star, (13)nuke, (14)stardisc, (15)nonagon, (16)sp'
        'ike(17)create your own, and (default)pick random.')
        pic = input()
    elif pic == '0':
        choices()
    elif pic == '1':
        left = 59
    elif pic == '2':
        left = 158.9
    elif pic == '3':
        left = 158.9
    elif pic == '4':
        left = 158.9
    elif pic == '5':
        left = 39
    elif pic == '6':
        left = 59
    elif pic == '7':
        left = 100.9351
    elif pic == '8':
        left = 239
    elif pic == '9':
        left = 90.2
    elif pic == '10':
        left = 542
    elif pic == '11':
        left = 280
    elif pic == '12':
        left = 200
    elif pic == '13':
        left = 200
    elif pic == '14':
        left = 140
    elif pic == '15':
        left = 170
    elif pic == '16':
        left = 170
    elif pic == '17':
        left = input()
        custompic = True
    else:
        pic = randint(1, 15)
        if pic == 1:
            left = 59
        elif pic == 2:
            left = 158.9
        elif pic == 3:
            left = 158.9
        elif pic == 4:
            left = 158.9
        elif pic == 5:
            left = 39
        elif pic == 6:
            left = 59
        elif pic == 7:
            left = 100.9351
        elif pic == 8:
            left = 239
        elif pic == 9:
            left = 90.2
        elif pic == 10:
            left = 542
        elif pic == 11:
            left = 280
        elif pic == 12:
            left = 200
        elif pic == 13:
            left = 200
        elif pic == 14:
            left = 140
        elif pic == 15:
            left = 170
        elif pic == 16:
            custompic = True
    say('You can press anything for the default of whichever picture you want, or press 1 and make custom colors.')
    colors2 = input()
    if colors2 == 0:
        say('You can press anything for the default of whichever picture you want, or press 1 and make custom colors.')
        colors2 = input()
        pickcolors = False
    elif colors2 == 1:
        pickcolors = True
    else:
        pickcolors = False
        if pic == '1':
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        elif pic == '2':
            colors = ['gray', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']
        elif pic == '3':
            colors = ['black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black', 'blue' +
            'black', 'purple']
        elif pic == '4':
            colors = ['black', 'red', 'black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black' +
            'blue', 'black', 'purple']
        elif pic == '5':
            colors = ['black', 'red', 'black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black' +
            'blue', 'black', 'purple']
        elif pic == '6':
            colors = ['black', 'red', 'black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black' +
            'blue', 'black', 'purple']
        elif pic == '7':
            colors = ['black', 'red', 'black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black' +
            'blue', 'black', 'purple']
        elif pic == '8':
            colors = ['black', 'red', 'black', 'gray', 'black', 'orange', 'black', 'yellow', 'black', 'green', 'black' +
            'blue', 'black', 'purple']
        elif pic == '9':
            colors = ['black']
        elif pic == '10':
            colors = []
        elif pic == '11':
            colors = []
        elif pic == '12':
            colors = []
        elif pic == '13':
            colors = []
        elif pic == '14':
            colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    return(left)

def draw(left):
    colors = ['#fff000']
    t = turtle.Pen()
    t.speed(0.5)
    for x in range(600):
        print(x)
        t.pencolor(colors[x % 6])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(left)
    print('Type "stop" to continue')
    keepdrawing()

def main():
    left = choices()
    draw(left)

main()
#cone(original): colors=rainbow(purple-red), x%6, left590
#illusion1: colors[0]=gray, x%7, left158.9
#illusion2: illusion1 with black every alternate in colors ( times) (starting at [0]), no red, x%12
#illusion3: illusion2 with red and black before it, x%14
#spiral1: same colors as illusion3, left39
#sixsidedspiral: same colors as illusion3, left59
#hexagonball1: same colors as illusion3, left100.9351
#illuminati: same colors as illusion3, left239
#pyramid1: all colors black, left90.2
#fans1: first 6 colors of illusion3, left542
#ninecorners1: same colors as fans1, left280
#star1: colors=black and yellow, left200
#nuke1: star1 with [2]=yellow in colors
#stardisc1: same colors as cone, left140
#spike: left170