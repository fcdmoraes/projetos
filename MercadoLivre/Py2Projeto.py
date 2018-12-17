from tkinter import *
import requests
from bs4 import BeautifulSoup

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
				item(nome,link,preço)
	try:
		url = soup.find('li', class_ = "pagination__next").a['href']
		buscar(url)
	except:
		print(len(item.items))
		print(item.items)

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
