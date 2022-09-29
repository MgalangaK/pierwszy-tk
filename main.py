from tkinter import Tk,Label,Button

root = Tk()
root.minsize(250,250)

lb1=Label()
lb1["text"] = "label 1 :)"
lb1.pack()


lb2=Label()
lb2.config(text="label 2 :)")
lb2.pack()


btn = Button()
btn.config(text="przycisk")
btn.pack()

root.mainloop()