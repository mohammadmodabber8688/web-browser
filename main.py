from window import windowmanager
import tkinter as tk
import turtle as tu


def windowinit():

    hieght = tk.IntVar()
    wight = tk.IntVar()
    
    #T = tu.Turtle()
    #Sc = tu.Screen()
    #hieght = input("import hieght: ")
    #wight = input("import wight: ")

    hieght = 500
    wight = 1000

    windowmanager.windowmanager(hieght,wight)

windowinit()
