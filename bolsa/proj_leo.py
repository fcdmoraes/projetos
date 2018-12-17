import csv
from datetime import datetime
import math
from tkinter import *
from PIL import Image,ImageTk

dados = []
header = []
def leitura(fundo):
    global header,dados
    dados = []
    arq = open(str(fundo)+'.csv','r',encoding='utf8')
    reader = csv.reader(arq)
    header = reader.__next__()
    for row in reader:
        dados.append(row)
    arq.close()
    data_converter()
def data_converter():
    for row in dados:
        row[0] = datetime.strptime(row[0],'%d/%m/%Y')
        for i in range(1,10):
            if i == 3:
                row[i] = float(row[i])
            else:
                row[i] = int(row[i].replace('.',''))
def maior_variacao():
    variacao = -99.99
    maior_var = dados[0]
    for row in dados:
        if row[3] > variacao:
            maior_var = row
            variacao = row[3]
    return maior_var
def menor_variacao():
    variacao = 99.99
    menor_var = dados[0]
    for row in dados:
        if row[3] < variacao:
            maior_var = row
            variacao = row[3]
    return maior_var
def rent_diaria():
    i = 1
    rent_diaria = []
    while i < len(dados):
        rent_diaria.append((dados[i][6]-dados[i-1][6])/dados[i-1][6])
        i+=1
    return rent_diaria
def media(lista):
    return sum(lista)/len(lista)
def desv_pd(lista):
    soma = 0
    med = media(lista)
    for i in lista:
        soma += (i-med)**2
    return math.sqrt(soma/len(lista))
def vol_diaria():
    rent = rent_diaria()
    return desv_pd(rent)
def vol_anual():
    return vol_diaria()*math.sqrt(252)
def info(fundo):
    try:
        leitura(fundo)
        jan = Toplevel(tk)
        jan.winfo_toplevel().title(fundo)

        Label(jan,text="Dados de "+fundo).grid(row = 0, column = 0, columnspan = 2, pady = 10)        
        
        Label(jan,text="Maior Variação:").grid(row = 1, column = 0)
        Label(jan,text = str(maior_variacao()[3])).grid(row = 1, column = 1)

        Label(jan,text="Menor Variação:").grid(row = 2, column = 0)
        Label(jan,text = str(menor_variacao()[3])).grid(row = 2, column = 1)

        vol_dia = "{0:.2f}".format(vol_diaria()*100)+"%"
        Label(jan,text="Volatilidade Diária:").grid(row = 3, column = 0)
        Label(jan,text = vol_dia).grid(row = 3, column = 1)

        vol_ano = "{0:.2f}".format(vol_anual()*100)+"%"        
        Label(jan,text="Volatilidade Anual:").grid(row = 4, column = 0)
        Label(jan,text = vol_ano).grid(row = 4, column = 1)

        Button(jan, text = 'Fechar', command = jan.destroy).grid(row = 5, columnspan = 2, pady = 10)
        
    except FileNotFoundError:
        jan = Toplevel(tk)
        Label(jan,text="Fundo não encontrado.").pack()

root = Tk()
root.option_add("*font", "Verdana", 12)
root.winfo_toplevel().title("")

header = Frame(root)
header.pack()

logo = Image.open("logo_lets_code_amarelo.png")
logo.resize((int(logo.width*0.5), int(logo.height*0.5)))
# print()
logo = ImageTk.PhotoImage(logo)
Label(header, image = logo).pack(pady = 10)
tk = Frame(root)
tk.pack()
# Label(tk,text='Fundo:').grid()
opt = ["IBOV","PETR4","VALE5","ITUB4","LREN3","HGTX3","GFSA3","BRKM5"]
var = StringVar(root)
var.set("Fundo:")
w = OptionMenu(tk, var, *opt)
w.config(width = 10)
w.pack(pady = 10, padx = 10)

dia = list(range(1,32))
mes = list(range(1,13))
ano = list(range(2017,2019))

Label(tk, text = "Data Inicial:").pack()
datai = Frame(tk)
datai.pack(padx = 10)

diai = StringVar(root)
diai.set("dia")
mesi = StringVar(root)
mesi.set("mês")
anoi = StringVar(root)
anoi.set("ano")
OptionMenu(datai,diai,*dia).grid(row = 0, column = 0, pady = 10)
OptionMenu(datai,mesi,*mes).grid(row = 0, column = 1)
OptionMenu(datai,anoi,*ano).grid(row = 0, column = 2)

Label(tk, text = "Data Final:").pack()
dataf = Frame(tk)
dataf.pack()

diaf = StringVar(root)
diaf.set("dia")
mesf = StringVar(root)
mesf.set("mês")
anof = StringVar(root)
anof.set("ano")
OptionMenu(dataf,diaf,*dia).grid(row = 0, column = 0, pady = 10)
OptionMenu(dataf,mesf,*mes).grid(row = 0, column = 1)
OptionMenu(dataf,anof,*ano).grid(row = 0, column = 2)

Button(tk,text="Gerar Info",command=lambda: info(var.get()), width = 13).pack()
Button(tk,text="Sair",command=root.destroy, width = 13).pack(pady = 10, padx = 10)

root.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")

root.mainloop()