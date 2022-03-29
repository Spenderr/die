from tkinter import *
from random import randint

die = { # the dictonary of the random elements to be rolled each time, these are all icons rather than pictures
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

App = Tk() #created a tkinter func here
App.title('Roll the die') # gave the window a title on this line
App.geometry('200x200') #here I have set the size of the window

dice = Label(App,  #this block is brought up when the program is run
             text=die[0], #we chose number 0 from our dictionary as the first text
             font = ( 'American Typewriter', 65), # I have set the font type and the size of it here
             foreground='black') #set the color of the dies

dice.grid(row=0,column=0,padx=25,pady=25) #here the dice is packed and the placement is set

def roll(): # a function which command the roll button to pick a random number each time the button is clicked
    i = randint(1,6) #radnint is a func from the random package and here it picks a random number between 1 and 6
    msg = Label(App ,
                text = die[i] , # the die dictionary is implemented and a random is called using 'i' as it randomizes
                font = ('American Typewriter',100), # I have set the font type and the size of it here
                foreground='black',#set the color of the dies
                width=2) # the width, here covers the first 'dice' label

    msg.grid(row=0 , column=0 , padx=25 , pady=5) # #here the msg is packed and the placement is set

rollButton = Button(App, # a simple roll button
                    text='Roll', #the button will display Roll on it
                    command=roll) #the command is imported from the line 25 here

rollButton.grid(row=1,column=0)

App.mainloop()
