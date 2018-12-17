import csv
produtos = {}

def leitura(arquivo):
	try:
		file = open(arquivo, 'r', encoding = 'utf8')
	except:
		return 0
	lista_produtos = csv.reader(file)
	lista_produtos = list(lista_produtos)
	file.close()
	while [] in lista_produtos:
		lista_produtos.remove([])
	print(lista_produtos)
	for i in range(len(lista_produtos)):
		Havaiana(lista_produtos[i][0], lista_produtos[i][1], lista_produtos[i][2], 
			lista_produtos[i][3], lista_produtos[i][4], lista_produtos[i][5], lista_produtos[i][6])

def salvar(arquivo):
	lista_produtos = []
	for nome in produtos:
		h = produtos[nome]
		for d in h.disponibilidade:
			dic = {'nome': h.nome, 'estampa': h.estampa, 'cor': d['cor'], 
			'tamanho': d['tamanho'], 'tira': h.tira, 'quantidade': d['quantidade'], 'preço': h.preço}
			lista_produtos.append(dic)
	print(lista_produtos)
	file = open(arquivo, 'w', encoding = 'utf8')
	headers = ['nome','estampa','cor', 'tamanho', 'tira', 'quantidade', 'preço']
	escritor = csv.DictWriter(file, fieldnames = headers)
	escritor.writerows(lista_produtos)
	file.close()

class Havaiana(object):
	def __init__(self, nome, estampa, cor, tamanho, tira = 'tradicional', quantidade = 0, preço = 0):
		if nome not in produtos:
			self.nome = nome
			self.tira = tira
			self.estampa = estampa
			self.disponibilidade = [{'cor': cor, 'tamanho': tamanho, 'quantidade': quantidade}]
			self.preço = preço
			produtos[nome] = self
		else:
			h = produtos[nome]
			for produto in h.disponibilidade:
				if produto['cor'] == cor and produto['tamanho'] == tamanho:
					produto['quantidade'] += quantidade
					return None
			h.disponibilidade.append({'cor': cor, 'tamanho': tamanho, 'quantidade': quantidade})

# H1 = Havaiana('H1', 'lisa', 'branca', '43')
# print(H1.disponibilidade)
# Havaiana('H1', 'lisa', 'branca', '42', quantidade = 10)
# print(H1.disponibilidade)
# salvar('teste.csv')