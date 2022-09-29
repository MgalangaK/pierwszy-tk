from tkinter import Tk,Label,Button, Entry

root = Tk()
root.minsize(250,250)

lb1=Label()
lb1["text"] = "label 1 :)"
lb1.grid(column=0, row=1)


lb2=Label()
lb2.config(text="label 2 :)")
lb2.grid(column=0, row=2)

def change_label2_on_click():
    lb2.config(text=entry.get())

btn = Button()
btn.config(text="przycisk", command=change_label2_on_click)
btn.grid(column=0, row=3)

entry = Entry()
entry.grid(column=0, row=4)



root.mainloop()