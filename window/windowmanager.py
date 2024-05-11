import tkinter as tk

Window = tk.Tk()

def windowmanager(a,b):

    
    Window.title = "Love"
    
    Window.geometry(f"{b}x{a}")
    
    Window.resizable(False,False)
    widgetmanager()

    Window.mainloop()

def widgetmanager():

    textbox = tk.Entry(Window)
    textbox.bind("<Return>", textmanager(textbox))
    textbox.place(x=10,y=10,width=500,height=10)
    textbox.pack()
    print(textfromtextbox1)

def textmanager(textbox):
    global textfromtextbox1

    textfromtextbox1 = textbox.get()

    