from tkinter import *

def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))

w = Tk()
Label(w, text="Your Math Expression:").pack()

entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()

res = Label(w)
res.pack()

w.mainloop()