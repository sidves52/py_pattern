import turtle

def keepdrawing():
    stop = 1
    while stop == 1:
        stop = input()

colors = input('colors: ').split()
left = int(input('degrees left: '))

def draw(left, colors):
    t = turtle.Pen()
    t.speed(0.5)
    for x in range(600):
        print(x)
        t.pencolor(colors[x % len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(left)
    print('Type anything to continue')
    keepdrawing()

draw(left, colors)
#cone(original): colors=rainbow(purple-red), x%6, left590
#illusion1: colors[0]=gray, x%7, left158.9
#illusion2: illusion1 with black every alternate in colors ( times) (starting at [0]), no red, x%12
#illusion3: illusion2 with red and black before it, x%14
#spiral1: same colors as illusion3, left39
#sixsidedspiral: same colors as illusion3, left59
#hexagonball: same colors as illusion3, left100.9351
#illuminati: same colors as illusion3, left239
#pyramid: all colors black, left90.2
#fans: first 6 colors of illusion3, left542
#ninecorners1: same colors as fans1, left280
#star: colors=black and yellow, left200
#nuke: star1 with [2]=yellow in colors
#stardisc: same colors as cone(or #0eddef), left140