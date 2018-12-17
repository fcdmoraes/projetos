from tkinter import *
from survey import *
# lista1 = [['Lula', 0], ['Alckimin', 0], ['Bolsonaro', 0], ['Boulos', 0], ['Ciro', 0], ['Branco ou Nulo',0]]
# lista2 = [['Lula', 0, 'Alckimin', 0, 'Branco ou Nulo', 0],['Lula', 0, 'Bolsonaro', 0, 'Branco ou Nulo', 0]]

def start():
	escolhas = []
	def turno2(combinacao):
		def action():
			escolha1 = escolha.get()
			if escolha1 not in candidatos:
				escolha1 = 'Branco ou Nulo'
			escolhas.append(escolha1)
			frame_t2.destroy()
			var.set(1)

		var = IntVar()

		frame_t2 = Frame(janela_aux)
		frame_t2.pack()
		Label(frame_t2, text = 'Escolha um candidato \npara o segundo turno:').pack()
		escolha = StringVar()
		for candidato in combinacao:
			b = Radiobutton(frame_t2, text = candidato, variable = escolha, value = candidato)
			b.pack(anchor = W)
		Button(frame_t2, text = 'Prosseguir', command = action).pack(pady = 10, padx = 20)
		frame_t2.wait_variable(var)

	def turno1():
		def finaliza_t1():
			escolha1 = escolha.get()
			if escolha1 not in candidatos:
				escolha1 = 'Branco ou Nulo'
			escolhaT1(escolha1)
			frame_t1.destroy()
			combinacoes = monta_combinacoes()
			for combinacao in combinacoes:
				turno2(combinacao)
			escolhasT2(escolhas)
			janela_aux.destroy()

		if valida_cpf(cpf.get()) == False:
			valida['text'] = 'CPF inválido'
		else:
			frame_cpf.destroy()
			frame_t1 = Frame(janela_aux)
			frame_t1.pack()
			Label(frame_t1, text = 'Escolha um candidato \npara o primeiro turno:').pack()
			escolha = StringVar()
			OM = OptionMenu(frame_t1, escolha, *candidatos)
			OM.config(width = 10)
			OM.pack(pady = 10)
			Button(frame_t1, text = 'Prosseguir', command = finaliza_t1).pack(pady = 10, padx = 20)

	janela_aux = Toplevel()
	janela_aux.winfo_toplevel().title("eleicoes 2018")
	Label(janela_aux, text = "Let's Vote", font = ("Verdana", 15, 'bold'), width = 15).pack(pady = 20)
	frame_cpf = Frame(janela_aux)
	frame_cpf.pack()
	Label(frame_cpf, text = 'CPF:').pack()
	cpf = Entry(frame_cpf, width = 12)
	cpf.pack(pady = 10)
	valida = Label(frame_cpf, text = '')
	valida.pack()
	Button(frame_cpf, text = 'Prosseguir', command = turno1).pack(pady = 10, padx = 20)

def see():
	lista1, lista2 = importaresultados()
	print(lista1)
	janela_aux = Toplevel()
	janela_aux.winfo_toplevel().title("eleicoes 2018")
	Label(janela_aux, text = "Let's Vote", font = ("Verdana", 15, 'bold'), width = 15).pack(pady = 20)
	frame_result = Frame(janela_aux)
	frame_result.pack()
	Label(frame_result, text = 'Primeiro Turno:').pack()
	frame_t1 = Frame(frame_result)
	frame_t1.pack()
	i = 0
	for x in lista1:
		Label(frame_t1, text = x[0]).grid(row = i, column = 0, sticky = W)
		Label(frame_t1, text = x[1]).grid(row = i, column = 1, padx = 10)
		i += 1
	Label(frame_result).pack()
	Label(frame_result, text = 'Segundo Turno:').pack(pady = 10)
	for x in lista2:
		frame_t2 = Frame(frame_result)
		frame_t2.pack()
		Label(frame_t2, text = x[0]).grid(row = 0, column = 0, sticky = W)
		Label(frame_t2, text = x[1]).grid(row = 0, column = 1, padx = 10)
		Label(frame_t2, text = x[2]).grid(row = 1, column = 0, sticky = W)
		Label(frame_t2, text = x[3]).grid(row = 1, column = 1, padx = 10)
		Label(frame_t2, text = x[4]).grid(row = 2, column = 0, sticky = W)
		Label(frame_t2, text = x[5]).grid(row = 2, column = 1, padx = 10)
		Label(frame_t2).grid()

janela = Tk()
janela.winfo_toplevel().title("eleicoes 2018")
janela.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")
janela.option_add("*font", "Verdana", 12)

Label(janela, text = "Let's Vote", font = ("Verdana", 15, 'bold')).pack(pady = 20)
Button(janela, text = 'iniciar pesquisa', command = start).pack()
Button(janela, text = 'resultado parcial', command = see).pack(pady = 10, padx = 20)


janela.mainloop()