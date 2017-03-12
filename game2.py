from tkinter import *

def main():
    Width = 800
    Height = 500
    window = Tk()
    window.title('Bubble Blaster')
    c = Canvas(window, width=Width, height=Height, bg='darkblue')
    c.pack()
    play = 'yes'
    #while play == 'yes':
    #play_game()
    return window

#def play_game():
main()

