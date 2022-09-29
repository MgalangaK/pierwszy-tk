from tkinter import Tk,Label,Button, Entry
from turtle import width

root = Tk()
root.minsize(250,250)

lb1=Label()
lb1["text"] = "label 1 :)"
lb1["background"] = "red"
lb1.grid(column=0, row=1, columnspan=2)

lb2=Label()
lb2.config(text="label 2 :)")
lb2.grid(column=0, row=2)

def change_label2_on_click():
    lb2.config(text=entry.get())

btn = Button()
btn.config(text="przycisk", command=change_label2_on_click)
btn.grid(column=0, row=3)
btn.config(padx=40,pady=40)

def get_smaller_on_click():
    btn2["padx"] -=5
    btn2["pady"] -=5
    
    

btn2 = Button()
btn2.config(text="zmniejsze sie na kliknięcie", command=get_smaller_on_click)
btn2.grid(column=0, row=10)
btn2.config(padx=40,pady=40)

entry = Entry()
entry.grid(column=0, row=4, columnspan=2)


root.mainloop()