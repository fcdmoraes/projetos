import requests
from bs4 import BeautifulSoup

class Produto(object):
	lista = []
	departamentos = {}
	def __init__(self, nome, preco, link):
		self.nome = nome
		self.preco = preco
		self.link = link
		Produto.lista.append(self)


def buscar_item(item):
	url = "https://www.amazon.com.br{}".format(item)
	print(url)
	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'html.parser')
	# print(soup.prettify())
	containers = soup.find_all('div', class_ = 's-item-container')
	for container in containers:
		try:
			nome = container.h2.get_text()
			preco = container.find('span', class_ = 's-price').get_text()
			link = container.a['href']
			Produto(nome,preco,link)
		except:
			pass
	departamentos = soup.find('div', class_="a-expander-extend-container")
	lista_dep = departamentos.find_all('h4')
	if lista_dep == []:
		lista_dep = departamentos.find_all('a')	
	lista_dep = list(map(lambda dep: dep.get_text(), lista_dep))
	links_dep = departamentos.find_all('a')
	links_dep = list(map(lambda dep: dep['href'], links_dep))
	# print(lista_dep)
	# print(links_dep)
	dic_dep = {}
	for i in range(len(lista_dep)):
		dic_dep[lista_dep[i]] = links_dep[i]
	Produto.departamentos = dic_dep

# buscar_item("/s?k=geladeira")
# buscar_item("/cadeira-Cozinha/s?ie=UTF8&page=1&rh=i%3Akitchen%2Ck%3Acadeira")