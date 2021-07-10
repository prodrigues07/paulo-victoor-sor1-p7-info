

from tkinter import *
import tkinter.messagebox

def clicked():
    res = "Welcome, " + txt.get() + ". If you want to see our available products,\nplease click on 'show'. If you want to leave our system, click on 'quit'"
    lbl.configure(text=res)

    btn_2 = Button(window, text='Show', command=showProducts)
    btn_2.grid(row=10, column=1, pady=10)

    btn_3 = Button(window, text='Quit', command=window.quit)
    btn_3.grid(row=11, column=1, pady=10)

def showProducts():
    tkinter.messagebox.showinfo('Supermarket | Products', 'Check out our products on the prompt page!')

    def table(product, entry, left, stock, price, total):
        print("|{:<19s}|{:>13d}|{:>13d}|{:>13d}|{:>13.2f}|{:>13.2f}|".format(product, entry, left, stock, price, total))
        print("+-------------------+-------------+-------------+-------------+-------------+-------------+")

    print("+-------------------+-------------+-------------+-------------+-------------+-------------+")
    print("|{:<19s}|{:>13s}|{:>13s}|{:>13s}|{:>13s}|{:>13s}|".format('Lista de Produtos', 'QTD Entradas', 'QTD Saídas',
                                                                     'Saldo Estoque', 'Preço Unitário', 'Subtotal'))
    print("+-------------------+-------------+-------------+-------------+-------------+-------------+")
    table('Azeite de Oliva', 100, 40, 60, 21.90, 1314)
    table('Castanha do Pará', 100, 5, 95, 6.00, 300)
    table('Flocos de Aveia', 1000, 200, 800, 10.9, 872)
    table('Paçoca de Amedoim', 100, 8, 92, 1.5, 30)
    table('Panetone sem Gluten', 100, 60, 40, 17.3, 692)
    table('Pão Sírio Integral', 100, 70, 30, 5.9, 177)
    table('Polpa de Açaí', 100, 1, 99, 7.1, 639)
    table('Queijo Vegano', 100, 30, 70, 25, 1750)
    print("|{:<19s}|{:>13s}|{:>13s}|{:>13s}|{:>13s}|{:>13.2f}|".format('', '', '', '', 'Total:', 1750))
    print("+-------------------+-------------+-------------+-------------+-------------+-------------+")

window = Tk()
window.title("Supermarket | Products")
window.geometry('500x400')

lbl = Label(window, text="Hello, this is Atacadao Market's System.\nWe need you to tell us who you are! Please, enter"
                         "your name: ")
lbl.grid(column=1, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=2, pady=8)

btn_1 = Button(window, text="Insert name", command=clicked)
btn_1.grid(column=1, row=3, pady=10)

window.mainloop()