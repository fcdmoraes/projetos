from tkinter import*
import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import ttk
from collections import Counter
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

MIN = 13

arquivo = open('palavras.txt', 'r', encoding = 'utf8')
linha = arquivo.read()
palavras_comuns = linha.split(',')
arquivo.close()

url = "https://programathor.com.br/jobs"
print(url)
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, 'html.parser')

skills = (soup.find("select").find_all("option"))
#skills2 = map(lambda s: s.get_text(),skills)
skills2 = []
for s in skills:
#	print(s)
	skills2.append(s.get_text())
#print(skills2)

contratos = soup.find_all('a', class_ = 'contract-tag')
#contratos2 = list(map(lambda c: c.get_text(), contratos))
contratos2 = []
for c in contratos:
	if c.get_text() not in contratos2:
		contratos2.append(c.get_text())
print(contratos2)

experiencia = soup.find_all('a', class_ = 'expertise-tag')
#experiencia2 = list(map(lambda c: c.get_text(), experiencia))
experiencia2 = []
for c in experiencia:
	if c.get_text() not in experiencia2:
		experiencia2.append(c.get_text())
print(experiencia2)

tamanho = soup.find_all('a', class_ = 'company-tag')
#tamanho2 = list(map(lambda c: c.get_text(), tamanho))
tamanho2 = []
for c in tamanho:
	if c.get_text() not in tamanho2:
		tamanho2.append(c.get_text())
print(tamanho2)

todas_vagas = []
def grafica():
	dados = pd.read_csv('resultado.csv', encoding = 'utf-8')
	print(dados.head())
	sns.countplot(data = dados, x = 'palavras')
	plt.show()

def salvar(palavras):
	arquivo = open('resultado.csv', 'w', encoding = 'utf8')
	arquivo.write('palavras\n')
	for palavra in palavras:
		arquivo.write(palavra.replace(',',''))
		arquivo.write('\n')
	arquivo.close()

def remover_comuns(palavras):
	for comum in palavras_comuns:
		while comum in palavras:
			palavras.remove(comum)

def busca_palavras():
	palavras = []
	n = len(todas_vagas)
	for (i, vaga) in enumerate(todas_vagas):
		os.system("clear")
		print("concluído: {:.2f}%".format(i/n*100))
		url = vaga['link']
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		texto = soup.find('div', class_ = "wrapper-content-job-show").get_text().lower()
		texto = texto.replace("/",' ')
		texto = texto.translate(texto.maketrans('','',',.()!?1234567890-%<>:'))
		palavras += texto.split()
	remover_comuns(palavras)
	contador = Counter(palavras)
	filtro = list(filter(lambda x: contador[x]>MIN, palavras))
	print(contador)
	salvar(filtro)

def crowler(url):
	global todas_vagas
	r = requests.get(url)
	print(url)
	print(r)
	soup = BeautifulSoup(r.text, 'html.parser')
	vagas = soup.find_all('div', class_ = 'cell-list')
	for vaga in vagas:
		nome = vaga.h3.get_text()
		link = 'https://programathor.com.br'+vaga.a['href']
		dic = {"nome": nome, 'link': link}
		todas_vagas.append(dic)
	try:
		next_page = soup.find('a', rel = 'Próx')
		crowler('https://programathor.com.br'+next_page['href'])
	except:
		return None

def buscar():
	sk = skill.get()
	ct = contract.get()
	ex = expertise.get()
	cp = company.get()
	print(sk,ct,ex,cp)
	url = 'https://programathor.com.br/jobs'
	if sk == skills2[0]:
		url += '?'
	else:
		url = url + '-' + sk.lower() + '?'
	if ct != '':
		url = url + 'contract_type=' + ct +'&'
	if ex != '':
		url = url + 'expertise=' + ex + '&'
	if cp != '':
		url = url + 'company_type=' + cp
	#webbrowser.open(url)
	crowler(url)
	print("vagas encontradas:", len(todas_vagas))
	busca_palavras()
	grafica()

root = Tk()
skill = StringVar(root)
skill.set(skills2[0])
contract = StringVar(root)
contract.set('Contrato')
expertise = StringVar(root)
expertise.set('Experiência')
company = StringVar(root)
company.set('Tamanho da Empresa')

OM1 = ttk.Combobox(root, textvariable = skill, values = skills2, justify = CENTER)
# OM1["values"] = skills2
OM1.pack(pady = 5, padx = 10, fill = X)
OM2 = OptionMenu(root,contract,'',*contratos2)
OM2.config(width = 20)
OM2.pack(pady = 5, padx = 10)
OM3 = OptionMenu(root,expertise,'',*experiencia2)
OM3.config(width = 20)
OM3.pack(pady = 5, padx = 10)
OM4 = OptionMenu(root,company,'',*tamanho2)
OM4.config(width = 20)
OM4.pack(pady = 5, padx = 10)
Button(root, text = 'Buscar Vaga', bd = 2, command = buscar).pack(fill = X, padx = 10, pady = 5)

root.mainloop()