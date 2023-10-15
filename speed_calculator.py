from tkinter import *
from timeit import default_timer as timer
gui = Tk()
gui.geometry("450x200")
x=0
def game():
    global x,gui
    if x==0:
        gui.destroy()
        x+=1
    def result():
        if entry.get()== word:
            end= timer()
            answer = str(end-start)
            answer_label=Label(gui,text=answer,font="times 20")
            answer_label.place(x=100,y=150)
        else:
            answer_label=Label(gui,text="Wrong Input",font="times 20")
            answer_label.place(x=100,y=150)
    word = "codercave"
    start = timer()
    gui= Tk()
    gui.geometry("450x200")
    x3=Label(gui,text=word,font="times 20")
    x3.place(x=150,y=10)
    x3=Label(gui,text="Start Typing")
    x3.place(x=10,y=50)
    entry =Entry(gui)
    entry.place(x=280,y=55)
    button2=Button(gui,text="Done",command=result,width=12,bg="grey")
    button2.place(x=150,y=100)
    button3 = Button(gui,text="Try Again",command=game) 
    button3.place(x=250,y=100)
    gui.mainloop()   
x1= Label(gui,text="Lets Play The Game!")
x1.place(x=10,y=50)
x2= Button(gui,text="Go",command=game,width=12,bg="grey")
x2.place(x=150,y=100)
gui.mainloop()
