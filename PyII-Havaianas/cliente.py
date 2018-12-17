from tkinter import *
import havaiana
cores = ['Outra']
tamanhos = list(range(30,45)) + ['Outro']

havaiana.leitura('havaianas.csv')

# print(havaiana.produtos)
def filtrar():
	# if cor.get() == 'Outra':
	# 	cor.set(cor_outra.get())
	# 	cores.append(cor.get())
	# 	OM3.update()
	# if tamanho.get() == 'Outro':
	# 	tamanho.set(tamanho_outro.get())
	# 	tamanhos.append(tamanho.get())
	# 	OM4.update(
	selecionados = []
	for modelo in havaiana.produtos:
		hav = havaiana.produtos[modelo]
		print('tira:', hav.tira)
		print('estampa', hav.estampa)
		print('\n')
		if (hav.tira == tira.get()) and (hav.estampa == estampa.get()):
			selecionados.append(hav)
	print(selecionados)

janela = Tk()

janela.winfo_toplevel().title('Loja Havainas')

Label(janela, text = 'Buscar produto').grid(row = 0, pady = 20)

# Label(janela).grid()
tira = StringVar(janela)
tira.set('Tira')
OM = OptionMenu(janela, tira, 'Tradicional','Larga','Sport','Casual')
OM.config(width = 15)
OM.grid(row = 3)

estampa = StringVar(janela)
estampa.set('Estampa')
OM2 = OptionMenu(janela, estampa, 'Lisa','Estampada')
OM2.config(width = 15)
OM2.grid(row = 4)

# cor = StringVar(janela)
# cor.set('Cor')
# OM3 = OptionMenu(janela, cor, *cores)
# OM3.config(width = 15)
# OM3.grid(row = 5)
# cor_outra = Entry(janela, width = 20)
# def ac1(*arg):
# 	if cor.get()=='Outra':
# 		cor_outra.grid(row = 6)
# 	else:
# 		cor_outra.grid_forget()
# cor.trace('w', ac1)

# tamanho = StringVar(janela)
# tamanho.set('Tamanho')
# OM4 = OptionMenu(janela, tamanho, *tamanhos)
# OM4.config(width = 15)
# OM4.grid(row = 7)
# tamanho_outro = Entry(janela, width = 20)
# def ac2(*arg):
# 	if tamanho.get() == 'Outro':
# 		tamanho_outro.grid(row = 8)
# 	else:
# 		tamanho_outro.grid_forget()
# tamanho.trace('w', ac2)

Button(janela, text = 'Buscar', width = 20, command = filtrar).grid(row = 14, pady = 20)

janela.mainloop()