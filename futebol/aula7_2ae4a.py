### PROJETO FUTEBOL ###
from tkinter import *
import csv

# aqui criamos duas lsitas: uma com o nome de todos os times, outra com os objetos do tipo time 
lista_times = []
lista_objetos = []

# aqui definimos a nossa classe time
class time():
	# assim que um objeto com classe time é criado, ele adiciona o nome do time na lista de times e o próprio objeto na lista de objetos
	def __init__(self, nome, gol_pro=0, gol_contra=0, soma_cartao_amarelo=0, soma_cartao_vermelho=0, vitoria=0, empate=0, derrota=0):
		self.nome = nome
		self.gol_pro = gol_pro
		self.gol_contra = gol_contra
		self.soma_cartao_amarelo = soma_cartao_amarelo
		self.soma_cartao_vermelho = soma_cartao_vermelho
		self.vitoria = vitoria
		self.empate = empate
		self.derrota = derrota
		lista_objetos.append(self)
		lista_times.append(nome)
	# a função cria_lista serve para criar uma lista com todas as características do time. Nós usamos essa lista para salvar em um arquivo .csv
	def cria_lista(self):
		self.lista = [self.nome, self.gol_pro, self.gol_contra, 
		self.soma_cartao_amarelo, self.soma_cartao_vermelho, 
		self.vitoria, self.empate, self.derrota]
	# a função atualiza recebe as informações de uma partida realizada pelo objeto de classe time e atualiza as propriedades desse objeto de acordo com o resultado da partida
	def atualizar(self, cartao_amarelo, cartao_vermelho, placar1, placar2):
		self.gol_pro += placar1
		self.gol_contra += placar2
		self.soma_cartao_amarelo += cartao_amarelo
		self.soma_cartao_vermelho += cartao_vermelho
		if placar1 > placar2:
			self.vitoria += 1
		elif placar1 == placar2:
			self.empate += 1
		else:
			self.derrota += 1
	# calcula os pontos de um time com base no seu número de vitórias e empates
	def pontos(self):
		pontos = (self.vitoria * 3) + self.empate
		return pontos

# essa função recebe todos os dados de uma partida e atualiza os times que participaram dela
def ResultIn(janela_r,t1,t2,p1,p2,ca1,ca2,cv1,cv2):
	# primeiramente fechamos a janela anterior
	janela_r.destroy()
	# em seguida, procuramos na lista de objeto, quais os times tem o mesmo nome que os times que jogaram a partida, e salvamos estes objetos nas variáveis Time1 e Time2
	for objeto in lista_objetos:
		if objeto.nome == t1:
			Time1 = objeto
		if objeto.nome == t2:
			Time2 = objeto
	# porfim, chamamos a função atualiza, interna do Time1 e do Time2, para atualizar suas propriedades com base no resultado da partida
	Time1.atualizar(int(ca1), int(cv1), int(p1), int(p2))
	Time2.atualizar(int(ca2), int(cv2), int(p2), int(p1))

# esta função cria uma janela onde o usuário entra com os dados de uma partida
def resultados():
	janela_r = Toplevel()
	frame1 = Frame(janela_r)
	frame1.pack(pady = 15)
	Label(frame1, text = "time 1").grid(column = 0, row = 0)
	# time1 = Entry(janela_r)
	nome_t1 = StringVar(janela_r)
	nome_t1.set("Time 1")
	time1 = OptionMenu(frame1, nome_t1, *lista_times)
	time1.config(width=10)
	time1.grid(column = 0, row = 1, padx = 5, pady = 5)

	Label(frame1, text = "time 2").grid(column = 1, row = 0)
	# time2 = Entry(janela_r)
	nome_t2 = StringVar(janela_r)
	nome_t2.set("Time 2")
	time2 = OptionMenu(frame1, nome_t2, *lista_times)
	time2.config(width=10)
	time2.grid(column = 1, row = 1, padx = 5)

	Label(frame1, text = "placar").grid(column = 0, row = 2, columnspan = 2)

	frame_p = Frame(frame1)
	frame_p.grid(column = 0, row = 3, columnspan = 2)
	placar1 = Entry(frame_p, width = 5)
	placar1.grid(column = 0, row = 0)
	Label(frame_p, text = "x").grid(column = 1, row = 0)
	placar2 = Entry(frame_p, width = 5)
	placar2.grid(column = 2, row = 0)

	Label(frame1, text = "CA").grid(column = 0, row = 4, columnspan = 2)
	CA1 = Entry(frame1, width = 5)
	CA1.grid(column = 0, row = 5)
	CA2 = Entry(frame1, width = 5)
	CA2.grid(column = 1, row = 5)

	Label(frame1, text = "CV").grid(column = 0, row = 6, columnspan = 2)
	CV1 = Entry(frame1, width = 5)
	CV1.grid(column = 0, row = 7)
	CV2 = Entry(frame1, width = 5)
	CV2.grid(column = 1, row = 7)

	Label(frame1).grid(column = 0, row = 8)
	Button(frame1, text = "Salvar Resultado", command = lambda: ResultIn(janela_r, nome_t1.get(), nome_t2.get(), placar1.get(), placar2.get(), CA1.get(), CA2.get(), CV1.get(), CV2.get())).grid(column = 0, row = 9, columnspan = 2)
	Label(frame1).grid(column = 0, row = 10)

# essa função importa os dados de um arquivo .csv e cria com as propriedades da tabela
def importar():
	file = open("tabela.csv", 'r', encoding = 'utf8')
	leitor = list(csv.reader(file))
	while [] in leitor:
		leitor.remove([])
	leitor.pop(0)
	for t in leitor:
		time(t[0],int(t[1]),int(t[2]),int(t[3]),int(t[4]),int(t[5]),int(t[6]),int(t[7]))
	file.close()

# essa função apaga todos os itens das listas de times e de objetos
def apagar():
	while len(lista_times)>0:
		lista_objetos.pop(0)
		lista_times.pop(0)
	print("delted")
	print(lista_times)

# essa função cria uma janela onde o usuário pode adicionar times na lista de times, importar um arquivo, ou apagar as informações salvas
def editar_times():
	janela_n = Toplevel()
	Label(janela_n, text = "nome do time").pack()
	time_novo = Entry(janela_n, bg='#f4d039', fg = '#2c465b', justify = CENTER, width = 12)
	time_novo.pack()
	Button(janela_n, text = "criar time", bg='#f4d039', fg = '#2c465b', command = lambda: time(time_novo.get())).pack(pady = 10)
	Button(janela_n, text = "Importar Arquivo", bg='#f4d039', fg = '#2c465b', command = importar).pack(pady = 10, padx = 10)
	Button(janela_n, text = "Apagar Tudo", bg='#f4d039', fg = '#2c465b', command = apagar).pack(pady = 10)

# essa função salva os dados de todos os times em um arquivo.csv
def salvar():
	# primeiramente criamos uma linha com o nome das informações a serem salvas
	tab = [["nome","gp","gc","ca","cv","v","e","d"]]
	# em seguida, olhamos cada objeto na lista de objetos e chamamos sua função interna que cria uma lista com todas as suas propriedades
	for time in lista_objetos:
		time.cria_lista()
		# depois adicionamos esta lista em uma lista de listas, chamada tab
		tab.append(time.lista)
	# profim, escrevemos todas as listas de tab em um arquivo .csv
	file = open("tabela.csv", "w", encoding = 'utf8')
	escritor = csv.writer(file)
	escritor.writerows(tab)
	file.close()

#função que faz a tabela do campeonato
def tabela():
	# primeiramente temos que ordenar a lista de objetos pelos critérios de quem está na frente do campeonato. Lembrando que como o número de pontos mais altos deve ser o primeiro, a lista é em ordem reversa
	lista_objetos.sort(key = lambda time: (time.pontos(), time.vitoria, time.gol_pro - time.gol_contra, time.gol_pro, -time.soma_cartao_vermelho, -time.soma_cartao_amarelo), reverse = True)
	t = Toplevel()
	i = 0
	# na primeira linha fazemos um label para cada elemento do cabeçalho, na ordem em que os valores serão inseridos
	for text in ["nome", "p", "v", "e", "d", "sg", "gp","cv","ca"]:
		Label(t, text = text).grid(column = i, row = 0)
		i += 1
	# a partir da primeira linha temos que imprimir os valores desejados de cada time da lista de objetos
	i = 1
	for time in lista_objetos:
		lista = time.cria_lista
		Label(t, text = time.nome).grid(column = 0, row = i)
		Label(t, text = str(time.pontos())).grid(column = 1, row = i)
		Label(t, text = str(time.vitoria)).grid(column = 2, row = i)
		Label(t, text = str(time.empate)).grid(column = 3, row = i)
		Label(t, text = str(time.derrota)).grid(column = 4, row = i)
		Label(t, text = str(time.gol_pro-time.gol_contra)).grid(column = 5, row = i)
		Label(t, text = str(time.gol_pro)).grid(column = 6, row = i)
		Label(t, text = str(time.soma_cartao_vermelho)).grid(column = 7, row = i)
		Label(t, text = str(time.soma_cartao_amarelo)).grid(column = 8, row = i)
		i+=1

#Aqui temos a janela principal
root = Tk()
root.geometry("300x300")
# mudando a cor padrão de todos os objetos:
root.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")
# mudando a font padrão de todos os textos
root.option_add("*font", "Verdana", 12)

frame1 = Frame(root)
frame1.pack(side = LEFT, fill = X, expand = 1)

Button(frame1, text = "Resultados", command = resultados, font=("Verdana", 20), background='#f4d039', foreground='#2c465b', width = 10).pack(pady = 5)
Button(frame1, text = "Editar", command = editar_times, font=("Verdana", 20), background='#f4d039', foreground='#2c465b', width = 10).pack(pady = 5)
Button(frame1, text = "Tabela", command = tabela, font=("Verdana", 20), background='#f4d039', foreground='#2c465b', width = 10).pack(pady = 5)
Button(frame1, text = "Salvar", command = salvar, font=("Verdana", 20), background='#f4d039', foreground='#2c465b', width = 10).pack(pady = 5)

root.mainloop()