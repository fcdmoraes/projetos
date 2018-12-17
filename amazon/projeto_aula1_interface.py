import projeto_aula1 as pf
from tkinter import *
import webbrowser

root = Tk()

def buscar(url):
	def filtrar():
		url = pf.Produto.departamentos[dep.get()]
		janela.destroy()
		buscar(url)
	pf.Produto.lista = []
	pf.buscar_item(url)
	janela = Toplevel()
	lista_itens = Frame(janela)
	lista_itens.pack()
	menu = Frame(janela)
	menu.pack()

	Label(lista_itens, text = "Nome", font = ('Arial',12,'bold')).grid(row = 0, column = 0, sticky = 'we')
	Label(lista_itens, text = "Preço", font = ('Arial',12,'bold')).grid(row = 0, column = 1, sticky = 'we')
	for i in range(len(pf.Produto.lista)):
		produto = pf.Produto.lista[i]
		Label(lista_itens, text = "{:<60.50}".format(produto.nome), anchor = 'w').grid(row = i+1, column = 0)
		Label(lista_itens, text = produto.preco).grid(row = i+1, column = 1)
		Button(lista_itens, text = "ir para o site", command = lambda n=i: webbrowser.open(pf.Produto.lista[n].link)).grid(row = i+1, column = 3)


	dep = StringVar()
	dep.set("{:40}".format("departamentos"))
	OM = OptionMenu(menu,dep,*pf.Produto.departamentos)
	OM.grid(row = 0, column = 0)
	Button(menu, text = 'filtrar', command = filtrar).grid(row = 0, column = 1)

	


frame = Frame(root)
frame.pack(padx = 10, pady = 10)
Label(frame, text = 'item:', anchor = 'w').pack(fill = X,)
item = Entry(frame, width = 20)
item.pack(pady = 5)
Button(frame, text = 'Buscar', command = lambda: buscar('/s?k='+item.get())).pack()

root.mainloop()
