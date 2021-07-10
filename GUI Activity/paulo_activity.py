# Infelizmente eu não consegui colocar a tabela em uma label
# Aqui eu não implementei o SQLite, só pra deixar mais simples. Então usuário e senha são: Admin, 123; respectivamente.

from tkinter import *
import tkinter.messagebox

def showProducts():
    def table(product, entry, left, stock, price, total):
        print("|{:<19s}|{:>13d}|{:>13d}|{:>13d}|{:>13.2f}|{:>12.2f}|".format(product, entry, left, stock, price, total))
        print("+-------------------+-------------+-------------+-------------+-------------+-------------+")

    print("+-------------------+-------------+-------------+-------------+-------------+-------------+")
    print("|{:<19s}|{:>13s}|{:>13s}|{:>13s}|{:>13s}|{:>12s}|".format('Lista de Produtos', 'QTD Entradas', 'QTD Saídas',
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

def loginProcess():
    userName = e1.get()
    passWord = e2.get()

    if (userName == '' and passWord == ''):
        tkinter.messagebox.showinfo('Login | Supermercado', 'Usuário e senha inválidos')

    elif (userName == 'Admin' and passWord == '123') or (userName == 'admin' and passWord == '123'):
        tkinter.messagebox.showinfo('Login | Supermercado', 'Login realizado!')
        window.destroy()
        root = Tk()
        root.title('Produtos | Supermercado')
        lbl = Label(root, text='Olá, Admin! Seja bem-vindo(a)!\nClique em "Mostrar" para verificar os produtos.')
        lbl.grid(column=1, row=0)

        btn_2 = Button(root, text='Mostrar', command=showProducts)
        btn_2.grid(row=10, column=1, pady=10)

        btn_3 = Button(root, text='Sair', command=root.quit)
        btn_3.grid(row=11, column=1, pady=10)

    else:
        tkinter.messagebox.showinfo('Login | Supermercado', 'Usuário e senha inválidos')

window = Tk()
window.title('Login | Supermercado')
window.geometry('190x80')
global e1
global e2

Label(window, text='Usuário: ').grid(row=0, sticky=W)
Label(window, text='Senha: ').grid(row=1, sticky=W)

e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=1, column=1)
e2.config(show='*')

btnLogin = Button(window, text='Login', command=loginProcess).grid(row=2, column=1, sticky=E)

window.mainloop()