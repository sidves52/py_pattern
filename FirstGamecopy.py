from tkinter import *
from random import randint
from math import sqrt
from time import sleep, time

Height = 500
Width = 800
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width = Width, height = Height, bg='darkblue')
c.pack()
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
ship_r = 15
mid_x = Width / 2
mid_y = Height / 2
c.move(ship_id, mid_x, mid_y)
c.move(ship_id2, mid_x, mid_y)

ship_speed = 10
def move_ship(event):
    if event.keysym == 'w':
        c.move(ship_id, 0, -ship_speed)
        c.move(ship_id2, 0, -ship_speed)
    elif event.keysym == 's':
        c.move(ship_id, 0, 20)
        c.move(ship_id2, 0, 20)
    elif event.keysym == 'a':
        c.move(ship_id, -ship_speed, 0)
        c.move(ship_id2, -ship_speed, 0)
    elif event.keysym == 'd':
        c.move(ship_id, ship_speed, 0)
        c.move(ship_id2, ship_speed, 0)
c.bind_all('<Key>', move_ship)

bub_id = list()
bub_r = list()
bub_spd = list()
min_bub_r = 10
max_bub_r = 30
max_bub_spd = 10
gap = 100
def create_bub():
    x = Width + gap
    y = randint(0, Height)
    r = randint(min_bub_r, max_bub_r)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white',)
    bub_id.append(id1)
    bub_r.append(r)
    bub_spd.append(randint(1,max_bub_spd))

bomb1_id = list()
def create_bomb1():
    x3 = Width + gap
    y3 = randint(0, Height)
    r2 = 12
    id2 = c.create_oval(x3 - r2, y3 - r2, x3 + r2, y3 + r2, outline='black', fill='darkgray', width=15)
    bomb1_id.append(id2)

def move_things():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_spd[i], 0)
    for i in range(len(bomb1_id)):
        c.move(bomb1_id[i], -11, 0)

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def pop_bub(i):
    del bub_r[i]
    del bub_spd[i]
    c.delete(bub_id[i])
    del bub_id[i]

def clean_up_bub():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -gap:
            pop_bub(i)

def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (ship_r + bub_r[bub]):
            points += (bub_r[bub] + bub_spd[bub])
            pop_bub(bub)
    return points

c.create_text(50, 30, text='TIME', fill='white')
c.create_text(150, 30, text='SCORE', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')
def show_score():
    c.itemconfig(score_text, text=str(score))
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))

bub_chance = 10
time_limit = 30
bonus_score = 1000
score = 0
bonus = 0
end = time() + time_limit

#main game loop
while time() < end:
    if randint(1, bub_chance) == 1:
        create_bub()
    #if randint(1, 30) == 1:
        create_bomb1()
    move_things()
    clean_up_bub()
    score += collision()
    if (int(score / bonus_score)) > bonus:
        bonus += 1
        end += time_limit
    show_score()
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

c.create_text(mid_x, mid_y, text='GAME OVER', fill='white', font=('Helvectica',30))
c.create_text(mid_x, mid_y + 30, text='Score: '+ str(score), fill='white')
c.create_text(mid_x, mid_y + 45, text='Bonus time: '+ str(bonus*time_limit), fill='white')

window.mainloop()