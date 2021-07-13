from tkinter import Tk, Entry, Button, END

# Criar janela e configurar
root = Tk()
root.iconbitmap("calc.ico")
root.title("Calculadora Simples")
root["bg"] = "silver"
root.resizable(height = False, width = False)

# Local para inserir texto
e = Entry(root, width=35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# função para botões
def button_click(num):
    atual = e.get()
    e.delete(0, END) # limpa o espaço
    e.insert(0,  str(atual) + str(num) )
    
def button_clear():
    e.delete(0, END)

def button_add():
    valor1 = e.get()
    global valor2
    global math
    math = 'add'
    valor2 = int(valor1)
    e.delete(0, END)

def button_mult():
    valor1 = e.get()
    global valor2
    global math
    math = 'mult'
    valor2 = int(valor1)
    e.delete(0, END)

def button_sub():
    valor1 = e.get()
    global valor2
    global math
    math = 'sub'
    valor2 = int(valor1)
    e.delete(0, END)

def button_div():
    valor1 = e.get()
    global valor2
    global math
    math = 'div'
    valor2 = int(valor1)
    e.delete(0, END)

def button_eq():
    valor1 = e.get()
    e.delete(0, END)

    if math == 'add':
        e.insert(0, int(valor2) + int(valor1))

    if math == 'sub':
        e.insert(0, int(valor2) - int(valor1))

    if math == 'mult':
        e.insert(0, int(valor2) * int(valor1))

    if math == 'div':
        try:
            e.insert(0, int(valor2) / int(valor1))
        except ZeroDivisionError:
            msg = 'Erro! Divisão por zero!'
            e.insert(0, msg)
    
#Botões numéricos
botao_1 = Button(root, text="1",padx=40, pady=20, command= lambda: button_click(1))
botao_2 = Button(root, text="2",padx=40, pady=20, command= lambda: button_click(2))
botao_3 = Button(root, text="3",padx=41, pady=20, command= lambda: button_click(3))
botao_4 = Button(root, text="4",padx=40, pady=20, command= lambda: button_click(4))
botao_5 = Button(root, text="5",padx=40, pady=20, command= lambda: button_click(5))
botao_6 = Button(root, text="6",padx=41, pady=20, command= lambda: button_click(6))
botao_7 = Button(root, text="7",padx=40, pady=20, command= lambda: button_click(7))
botao_8 = Button(root, text="8",padx=40, pady=20, command= lambda: button_click(8))
botao_9 = Button(root, text="9",padx=41, pady=20, command= lambda: button_click(9))
botao_0 = Button(root, text="0",padx=40, pady=20, command= lambda: button_click(0))
#Outros botões
button_add = Button(root, text="+", padx=39, pady=20, command = button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command = button_sub)
button_mult = Button(root, text="x", padx=41, pady=20, command = button_mult)
button_div = Button(root, text="/", padx=41, pady=20, command = button_div)
button_eq = Button(root,bg="#a2b4e0",text="=", padx=85, pady=20, command = button_eq)
button_clear = Button(root,bg="#ffef96",text='C', padx = 74, pady = 20, command = button_clear)

#colocar os botões na tela
botao_1.grid(row= 3, column= 0) 
botao_2.grid(row= 3, column= 1) 
botao_3.grid(row= 3, column= 2) 
botao_4.grid(row= 2, column= 0) 
botao_5.grid(row= 2, column= 1) 
botao_6.grid(row= 2, column= 2) 
botao_7.grid(row= 1, column= 0) 
botao_8.grid(row= 1, column= 1) 
botao_9.grid(row= 1, column= 2) 
botao_0.grid(row= 4, column= 0) 

button_add.grid(row = 5, column = 0)
button_sub.grid(row = 6, column = 0)
button_mult.grid(row = 6, column = 1)
button_div.grid(row = 6, column = 2, sticky='we')
button_clear.grid(row = 4, column = 1, columnspan = 2, sticky="we") 
button_eq.grid(row = 5, column = 1, columnspan = 2, sticky="we") 

root.mainloop()

