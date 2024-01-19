#name: Phil Liu
#PA5 Fifteen 
#game.py module

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

def clickButton(button):

    if button.cget("text") != " ":
        if button.cget("text") == "shuffle":
            shuffle(100)
            return

        if tiles.is_valid_move(int(button.cget("text"))):

            tiles.update(int(button.cget("text")))
            buttonRow = button.grid_info()['row']
            buttonColumn = button.grid_info()['column']
            emptyRow = button16.grid_info()['row']
            emptyColumn = button16.grid_info()['column']
            button.grid_forget()
            button16.grid_forget()
            button.grid(row=emptyRow, column=emptyColumn)
            button16.grid(row = buttonRow, column= buttonColumn)

        if tiles.is_solved():
            print('You win!')
            exit()



def shuffle(count):
    tiles.shuffle(count)
    j = 0
    for i in tiles.tiles:
        if i == 0:
            button = gui.nametowidget("16")
            button.grid(row=j // 4, column=j % 4)
        else:
            button = gui.nametowidget(str(i))
            button.grid(row=j // 4, column=j % 4)
        j += 1



if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    buttons = []

    # Using loop to create the first 15 buttons
    for i in range(1, 16):
        text = StringVar()
        text.set(str(i))
        button = Button(gui, textvariable=text, name=str(i),
                        bg='white', fg='black', font=font,
                        height=2, width=5, command=lambda i=i: clickButton(buttons[i-1]))
        button.configure(bg='coral')
        button.grid(row=(i-1) // 4, column=(i-1) % 4)
        buttons.append(button)

    # Defining empty space
    text16 = StringVar()
    text16.set(' ')
    name16 = '16'
    button16 = Button(gui, textvariable=text16, name=name16,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda: clickButton(button16))
    button16.configure(bg='white')
    button16.grid(row=3, column=3)

    # Defining shuffle button
    text17 = StringVar()
    text17.set('shuffle')
    name17 = 'shuffle'
    button17 = Button(gui, textvariable=text17, name=name17,
                      bg='white', fg='black', font=font,
                      height=2, width=20, command=lambda: clickButton(button17))
    button17.configure(bg='white')
    button17.grid(row=4, columnspan=5)

    gui.mainloop()