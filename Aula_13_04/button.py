# from tkinter import *
# master = Tk()
#
# def var_states():
#     print("English: %d,\nSpanish: %d" % (var1.get(), var2.get()))
#
# Label(master, text="Your languages:").grid(row=0, sticky=W)
# var1 = IntVar()
# Checkbutton(master, text="english", variable=var1).grid(row=1, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='spanish', variable=var2).grid(row=2, sticky=W)
# Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
# Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
# mainloop()

import tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()