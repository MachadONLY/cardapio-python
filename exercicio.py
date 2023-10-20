from tkinter.ttk import *
from tkinter import *

def calcular_total():
    lanche = comboLanche.get()
    porcao = comboPorcao.get()
    bebida = comboBebida.get()

    # Mapeie os itens selecionados para seus respectivos preços
    precos = {
        "Burger": 10.00,
        "Noodles": 8.00,
        "Pizza": 12.00,
        "Fritas": 4.00,
        "Nuggets": 6.00,
        "Milho": 3.00,
        "Suco": 2.00,
        "Shake": 3.50
    }

    # Calcule o total
    total = precos[lanche] + precos[porcao] + precos[bebida]

    # Atualize a imagem exibida com base nas escolhas
    label1.config(image=escolha_imagens[lanche])
    label2.config(image=escolha_imagens[porcao])
    label3.config(image=escolha_imagens[bebida])

    # Atualize o rótulo de preço total
    preco_total.config(text=f"Total a ser pago: R$ {total:.2f}")

window = Tk()
window.title("Escolha seu combo")
window.geometry("700x800")
container1 = Frame(window)
container1.pack()

rotuloLanche = Label(container1, text="Lanche")
rotuloLanche["font"] = ("", "12", "bold")
rotuloLanche.pack(side=LEFT)
comboLanche = Combobox(container1)
comboLanche["values"] = ("Burger", "Noodles", "Pizza")
comboLanche.current(0)
comboLanche.pack(side=LEFT, padx=10)

container2 = Frame(window)
container2.pack()

rotuloPorcao = Label(container2, text="Porção")
rotuloPorcao["font"] = ("", "12", "bold")
rotuloPorcao.pack(side=LEFT)
comboPorcao = Combobox(container2)
comboPorcao["values"] = ("Fritas", "Nuggets", "Milho")
comboPorcao.current(0)
comboPorcao.pack(side=LEFT, padx=10)

container3 = Frame(window)
container3.pack()

rotuloBebida = Label(container3, text="Bebida")
rotuloBebida["font"] = ("", "12", "bold")
rotuloBebida.pack(side=LEFT)
comboBebida = Combobox(container3)
comboBebida["values"] = ("Suco", "Shake")
comboBebida.current(0)
comboBebida.pack(side=LEFT, padx=10)

containerImagens = Frame(window)
containerImagens.pack()

escolha_imagens = {
    "Burger": PhotoImage(file="./cardapio/burger.png"),
    "Noodles": PhotoImage(file="./cardapio/noodles.png"),
    "Pizza": PhotoImage(file="./cardapio/pizza.png"),
    "Fritas": PhotoImage(file="./cardapio/fritas.png"),
    "Nuggets": PhotoImage(file="./cardapio/nuggets.png"),
    "Milho": PhotoImage(file="./cardapio/milho.png"),
    "Suco": PhotoImage(file="./cardapio/suco.png"),
    "Shake": PhotoImage(file="./cardapio/shake.png")
}

label1 = Label(containerImagens, image=escolha_imagens["Burger"])
label2 = Label(containerImagens, image=escolha_imagens["Fritas"])
label3 = Label(containerImagens, image=escolha_imagens["Suco"])
label2.pack(side=LEFT, padx=20, pady=60)
label3.pack(side=LEFT, padx=20, pady=60)
label1.pack(side=LEFT, padx=20, pady=60)

containerButton = Frame(window)
containerButton.pack()

botaoFazerPedido = Button(containerButton, text="Fazer Pedido", command=calcular_total)
botaoFazerPedido.pack()

preco_total = Label(window, text="Total a ser pago: R$ 0.00", font=("", 12, "bold"))
preco_total.pack()

window.mainloop()
