import pyttsx3
from tkinter import *
import tkinter as tk
from tkinter import ttk


class Root(Frame):
    def __init__(self):

        tk.Frame.__init__(self)
        self.pack()
        self.master.title('HOLY BIBLE')
        self.title('HOLY BIBLE')
        self.minsize(800, 400)


engine = pyttsx3.init()
win = Root()
win.mainloop()

def read(search, book):
    engine = pyttsx3.init()

    for u in book:
        if u[0:len(search) ].rstrip() == search:
            print(u)
            engine.say(u)
            engine.runAndWait()


while True:
    search = input('Please enter verse:\n e.g Genesis 1:20, Genesis, Genesis 5\n ')
    search.lstrip().rstrip()
    scripture = search.split(' ')[0].rstrip()
    text = str(open(scripture + '.txt', 'rt').read())
    book = text.split('\n')
    read(search, book)
    print(book)
