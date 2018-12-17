import interface
import random

def captura_palavra():
	arquivo = open("palavras.txt", 'r')
	lista = []
	for linha in arquivo:
		linha = linha.replace('\n','')
		lista.append(linha)
	arquivo.close()
	n = random.randint(0,len(lista)-1)
	return lista[n]

def atualiza(oculto, palavra, chute):
	nova = ''
	for i in range(len(palavra)):
		letra = palavra[i]
		if letra == chute:
			nova = nova + letra
		else:
			nova = nova + oculto[i]
	return nova

palavra = captura_palavra()
oculto = '#'*len(palavra)
jogo = interface.forca(oculto)

while True:
	if jogo.chutou() == True:
		chute = jogo.input()
		if chute in palavra:
			oculto = atualiza(oculto, palavra, chute)
			jogo.acertou(oculto)

		else:
			jogo.errou()
	jogo.update()
