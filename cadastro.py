import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Arroz", "Feijão", "Farinha", "Açucar"]
lista_codigos = []

janela = tk.Tk()

#Criação da função

def inserir_codigo(): #def é a forma do python identificar que eu estou criando uma função
   descricao = entry_descricao.get()
   tipo = combobox_selecionar_tipo.get()
   quantidade = entry_quantidade.get()
   data_criacao = dt.datetime.now()
   data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")   #Esse método é o que permite mudar o formato do date time para string
   codigo = len(lista_codigos)+1
   codigo_str = "COD-{}".format(codigo)
   lista_codigos.append((codigo_str, descricao, tipo, quantidade, data_criacao))


#Titulo da janela

janela.title('CPDT')

#Criação da janela
lable_descricao = tk.Label(text="Descrição do produto")
lable_descricao.grid(row=1, column=0, padx= 10, pady= 10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

lable_tipo_unidade = tk.Label(text="Tipo da unidade do produto")
lable_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

lable_quantidade = tk.Label(text="Quantidade na unidade do produto")
lable_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Gerar código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_codigos)