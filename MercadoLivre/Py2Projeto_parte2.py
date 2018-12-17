### MERCADO LIVRE ###
from tkinter import *
import requests
from bs4 import BeautifulSoup
import webbrowser
### NO MAC - COMENTAR A LINHA ABAIXO
import matplotlib.pyplot as plt
### NO MAC - DESCOMENTAR AS LINHAS ABAIXO
# import matplotlib
# matplotlib.use(“Agg”)
# import matplotlib.pyplot as plt

import numpy as np

root = Tk()

class item(object):
	items = []
	def __init__(self, nome, preço, link):
		self.nome = nome
		self.preço = preço
		self.link = link
		item.items.append(self)
		self.dict = {"nome": self.nome, 'preço': self.preço, "link": self.link}
	def __repr__(self):
		# return str(dict(self))
		return self.nome
	def __iter__(self):
			for key in self.dict:
				yield(key, self.dict[key])
	def histograma():
		preços = []
		for prod in item.items:
			preços.append(int(prod.preço.replace('.','')))
		preços = np.array(preços)
		plt.hist(preços, bins='auto')
		plt.title("Preços encontrados")
		plt.xlabel("Preço")
		plt.ylabel("Frequencia")
		plt.show()
		# plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')



class show_items():
	def __init__(self):
		self.pag = 0
		self.janela = Toplevel()
		self.results = Frame(self.janela)
		Label(self.results, text = "Nome").grid(column = 0, row = 0)
		Label(self.results, text = "Preço").grid(column = 1, row = 0)
		self.draw_results()
		navegate = Frame(self.janela)
		navegate.grid(row = 1)
		Button(navegate, text = '<<', command = self.prox).grid(row = 0, column = 0)
		Button(navegate, text = '>>', command = self.ant).grid(row = 0, column = 1)
		edit = Frame(self.janela)
		edit.grid(row = 2)
		remover = Entry(edit).grid(row = 0, column = 0)
		Button(edit, text = "Remover").grid(row = 0, column = 1)
		Button(edit, text = "Filtrar").grid(row = 0, column = 2)
		Button(edit, text = "Histograma", command = item.histograma).grid(row = 0, column = 3)

	def draw_results(self):
		self.results.destroy()
		self.results = Frame(self.janela)
		self.results.grid(row = 0) 
		for i in range(20):
			try:
				prod = item.items[i+20*self.pag]
				Label(self.results, text = prod.nome).grid(column = 0, row = i+1)
				Label(self.results, text = prod.preço).grid(column = 1, row = i+1)
				Button(self.results, text = 'ver no site', command = lambda x=prod.link: webbrowser.open(x)).grid(column = 2, row = i+1)
			except:
				pass
	def prox(self):
		self.pag += 1
		self.draw_results()
	def ant(self):
		self.pag -= 1
		self.draw_results()

def buscar(url):
	url=url.replace(' ','%20')
	print(url)
	r = requests.get(url)
	print(r)
	soup = BeautifulSoup(r.text, 'html.parser')
	i_info = soup.find_all('div', class_ = "item__info")
	for info in i_info:
		nome = info.a.get_text().replace("  ",'')
		link = info.a['href']
		preço = info.find("span", class_ = 'price__fraction').get_text()
		if contendo.get().lower() in nome.lower():
			if excluindo.get() == '' or excluindo.get().lower() not in nome.lower():
				item(nome,preço,link)
	try:
		url = soup.find('li', class_ = "andes-pagination__button--next").a['href']
		buscar(url)
	except:
		print(len(item.items))
		print(item.items)
		show_items()

Label(root, text = "Mercado Livre - Searcher", font = ("Lucida", 12, 'bold')).pack(pady = 10, padx = 20)
Label(root).pack()
frame = Frame(root)
frame.pack()
Label(frame, text = "Busca:").grid(sticky = 'w')
busca = Entry(frame)
busca.grid(sticky = 'w')
Label(frame).grid()
Label(frame, text = "Cotendo no nome:").grid(sticky = 'w')
contendo = Entry(frame)
contendo.grid(sticky = 'w')
Label(frame).grid()
Label(frame, text = "Não cotendo no nome:").grid(sticky = 'w')
excluindo = Entry(frame)
excluindo.grid(sticky = 'w')
Label(frame).grid()
Button(root, text = 'Buscar', command = lambda: buscar("https://lista.mercadolivre.com.br/"+ busca.get())).pack()
Label(root).pack()

root.mainloop()
