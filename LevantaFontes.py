import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from collections import Counter
from tkinter import *

candidato = "Marina Silva"
periodo = 'dia'

class fontes(list):
	def __init__(self):
		super(fontes, self).__init__()
	def add(self, lista):
		self += lista
	def relatorio(self):
		dic = dict(Counter(self))
		text = ''
		for fonte, num in sorted(dic.items(), key = lambda item: (item[1], item[0]), reverse = True):
			text += "{:.<60}{:.>3}\n".format(fonte,num)
		return text

def monta_link(candidato, período, inicio = '', fim = ''):
	url = 'https://www.google.com/search?q={}&tbm=nws&lr=lang_pt&tbs=qdr:'.format(candidato)

	if período == 'hora':
		url += 'h'
	elif período == 'dia':
		url += 'd'
	elif período == 'semana':
		url += 'w'
	elif período == 'mês':
		url += 'm'
	elif período == 'ano':
		url += 'y'
	else:
		if inicio != '':
			url += ',cd_min:{}'.format(inicio)
		if fim != '':
			url += ',cd_max:{}'.format(fim)
	return url

def crawler(url):
	# r = requests.get(url)
	# soup = BeautifulSoup(r.text, 'html.parser')
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')

	s_fontes = soup.find_all('span', class_ = 'xQ82C')
	# print(soup.prettify())

	fontes_text = list(map(lambda fonte: fonte.get_text(), s_fontes))
	resultado.add(fontes_text)
	print(fontes_text)
	try:
		prox = soup.find('a', id = 'pnnext')
		prox = 'https://www.google.com' + prox['href']
		return(prox)
	except:
		return None

def busca_fontes(npages = -1):
	link = monta_link(candidato, periodo)
	driver.get(link)
	root = Tk()
	root.mainloop()
	if npages == -1:
		while True:
			link = crawler(link)
			if link == None:
				break
	else:
		for i in range(npages):
			link = crawler(link)
			if link == None:
				break
	# j = 0
	# while j < npages or npages == -1:
	# 	link = crawler(link)
	# 	if link == None:
	# 		break
	# 	j += 1

def email(text):
	import smtplib
	import getpass

	my_email = 'flavio.moraes.lc@gmail.com'
	# senha = getpass.getpass('Digite sua senha: ')
	senha = 'programar123'

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(my_email,senha)

	assunto = 'Relatorio de candidato'
	remetente = 'ffllaa@gmail.com'
	msg = 'Subject: {}\n\n{}'.format(assunto, text)
	msg = msg.encode('utf8')
	server.sendmail(my_email, remetente, msg)
	server.quit()

resultado = fontes()

driver = webdriver.Chrome()
busca_fontes(3)
driver.quit()

email(resultado.relatorio())