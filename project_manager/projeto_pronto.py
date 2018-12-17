### GERENCIADOR DE PROJETOS ###
from tkinter import *
from operator import itemgetter
import csv
from PIL import Image, ImageTk

matriz = []

### função que importa um arquivo .csv
def importar():
	global matriz
	file = open("dados.csv", "r", encoding = "utf8")
	leitura = csv.reader(file)
	matriz = list(leitura)
	file.close()

### função que exporta um arquivo .csv
def exportar():
	file = open("dados.csv", "w", newline='', encoding = "utf8")
	escritor = csv.writer(file)
	escritor.writerows(matriz)
	file.close()

 ### função que insere um registro na matriz
def inserir_registro(projeto, tipo, valor, data):
	# escrever função #
	global matriz
	matriz.append([projeto, tipo, valor, data])
	matriz = sorted(matriz, key = itemgetter(0,1,3,2))

def campoInt(campo):
	if campo == "projeto":
		return 0
	elif campo == "tipo de gasto":
		return 1
	elif campo == "valor":
		return 2
	elif campo == "data":
		return 3
	else:
		return None

### função que busca um valor em um campo da matriz e cria uma nova matriz 'filtrados' com as linhas que contém o valor buscado
def buscar(campo,valor):
	filtrados = []
	for linha in matriz:
		if valor in linha[campoInt(campo)]:
			filtrados.append(linha)
	mostrar_dados(filtrados)

### função que, dado um campo, agrupa os itens iguais nesse campo, somando os valores
def sumarizar(campo):
	# escrever função #
	sumarizados = []
	matrizOrdCampo = sorted(matriz, key = itemgetter(campoInt(campo)))
	primeiraLinha = matrizOrdCampo[0] 
	valor = primeiraLinha[campoInt(campo)]
	total = 0
	for linha in matrizOrdCampo:
		LinhaSumarizada = ['','','','']
		if valor == linha[campoInt(campo)]:
			total += int(linha[campoInt("valor")])
		else:
			LinhaSumarizada[campoInt(campo)] = valor
			LinhaSumarizada[campoInt('valor')] = total
			sumarizados.append(LinhaSumarizada)
			valor = linha[campoInt(campo)]
			total = int(linha[campoInt('valor')])
			print(valor)
	LinhaSumarizada = ['','','','']
	LinhaSumarizada[campoInt(campo)] = valor
	LinhaSumarizada[campoInt('valor')] = total
	sumarizados.append(LinhaSumarizada)

	mostrar_dados(sumarizados)


### função que mostra uma matriz
def mostrar_dados(dados):
	janela_m = Toplevel()
	Label(janela_m).pack()

	frame = Frame(janela_m)
	frame.pack()
	Label(frame, text = "projeto").grid(row = 0 , column = 0, padx = 5)
	Label(frame, text = "tipo").grid(row = 0 , column = 1, padx = 5)
	Label(frame, text = "valor").grid(row = 0 , column = 2, padx = 5)
	Label(frame, text = "data").grid(row = 0 , column = 3, padx = 5)
	i = 0
	for linha in dados:
		i = i + 1
		for j in range(4):
			Label(frame, text = linha[j]).grid(row = i , column = j, padx = 5)

### função que pede os valores para inserir um dado
def inserir():
	janela_i = Toplevel()
	Label(janela_i).pack()

	Label(janela_i, text = "nome do projeto:").pack(pady = 2)
	projeto = Entry(janela_i)
	projeto.pack(pady = 2, padx = 10)
	Label(janela_i, text = "tipo de gasto:").pack(pady = 2)
	tipo = Entry(janela_i)
	tipo.pack(pady = 2, padx = 10)
	Label(janela_i, text = "valor do gasto:").pack(pady = 2)
	valor = Entry(janela_i)
	valor.pack(pady = 2, padx = 10)
	Label(janela_i, text = "data (aammdd):").pack(pady = 2)
	data = Entry(janela_i)
	data.pack(pady = 2, padx = 10)
	Button(janela_i, text = "inserir", command = lambda: inserir_registro(projeto.get(), tipo.get(), valor.get(), data.get())).pack(pady = 2)

### janela principal do programa
janela = Tk() # cria a janela principal

menu = Frame(janela, bg = "#f4d039", width=250, height = 44)
menu.pack(fill = X, expand = True)

logo = Image.open("logo.gif")
logo = logo.resize((int(logo.width*0.7),int(logo.height*0.7)))
logo = ImageTk.PhotoImage(logo)
Label(menu, bg = "#f4d039", image = logo).pack(fill = X)

Label(janela).pack() # Coloca um label vazio na janela (o único objetivo é ter um espaço vazio no topo da janela)


# a seguir iremos criar os botões. A função Button() cria um botão
# text indica qual texto está escrito no botão
# command indica qual função será chamada quando o botão for pressionado
# .pack() serve para encaixar esse botão na janela / pady serve para dar um espaçamento entre os items acima e abaixo 
Button(janela, text = "importar dados", command = importar, width = 15).pack(pady = 2, padx = 20) 
Button(janela, text = "inserir registro", command = inserir, width = 15).pack(pady = 2)
# como 'command = nome_da_função' não nos permite passar variáveis, só podemos chamar funções que não recebem variáveis
# para burlar isso podemos usar 'command = lambda: função(variáveis)' - não se preocupe em entender isso agora. A função lambda é assunto do curso de python 2 
Button(janela, text = "visualizar dados", command = lambda: mostrar_dados(matriz), width = 15).pack(pady = 2)
Button(janela, text = "exportar dados", command = exportar, width = 15).pack(pady = 2)

Label(janela).pack() # mais um label vazio para dar um espaço

# agora vamos criar a parte de busca nos registros
Label(janela, text = "Busca de Registro", width = 15).pack(pady = 2) # este label tem um texto dentro
# queremos criar um menu onde o usuário possa escolher em que coluna ele quer fazer a busca. Para isso precisamos de uma variável especial que vai armazenar essa informação
option1 = StringVar(janela) # option1 será a nossa variável. Ela é de um tipo especial, chamado StringVar
option1.set("buscar em") # aqui nós colocamos o texto que aparece no menu antes do usuário escolher
# em seguida nós criamos o menu indicando onde ele vai estar, qual variável vai armazenar a escolha, e quais são as escolhas possíveis
OM = OptionMenu(janela, option1, "projeto","tipo de gasto","valor","data")
OM.config(width = 12)
OM.pack(pady = 2)
# agora vamos criar uma entrada de texto onde o usuário pode escrever o que ele quer buscar
valor = Entry(janela, width = 15) #valor será onde o usuário vai digitar o que quer buscar
valor.pack(pady = 2, padx = 10) # colocamos a entrada na janela
Button(janela, text = "Buscar", command = lambda:buscar(option1.get(), valor.get()), width = 15).pack(pady = 2)

Label(janela).pack()

Label(janela, text = "Sumarizar Resgistros", width = 15).pack(pady = 2)
option2 = StringVar(janela)
option2.set("sumarizar sobre")
OM2 = OptionMenu(janela, option2, "projeto","tipo de gasto","data")
OM2.config(width = 12)
OM2.pack(pady = 2)
Button(janela, text = "Sumarizar", command = lambda:sumarizar(option2.get())).pack(pady = 10)

# Label(janela).pack()

# mudando a cor padrão de todos os objetos:
janela.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")

janela.mainloop()