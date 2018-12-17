import csv
candidatos = ['Lula', 'Alckimin', 'Bolsonaro', 'Boulos', 'Ciro', 'Marina', "Joao Amoedo", 'Flávio Rocha', 'Branco ou Nulo']

def multiplica(s,l):
	resultado = 0
	for i in range(len(s)):
		resultado += int(s[i])*l[i]
	return resultado*10%11

def valida_cpf(cpf):
	""" recebe um cpf em texto e verifica se é válido """
	cpf = cpf.replace('.','')
	cpf = cpf.replace('-','')
	file = open('cpf.dat', 'r', encoding = 'utf8')
	leitor = csv.reader(file)
	leitor = list(leitor)
	file.close()
	print(leitor)
	if [cpf] in leitor:
		return False
	else:
		if multiplica(cpf[0:9], range(10,1,-1)) != int(cpf[9]):
			return False
		if multiplica(cpf[0:10], range(11,1,-1)) != int(cpf[10]):
			return False
	file = open('cpf.dat', 'a', encoding = 'utf8')
	file.write(cpf+"\n")
	file.close()
	return True

def escolhaT1(escolha):
	""" recebe a preferência do usuário no primeiro turno e salva em um arquivo """
	file = open('turno1', 'r', encoding = 'utf8')
	leitor = csv.reader(file)
	leitor = list(leitor)
	while [] in leitor:
		leitor.remove([])
	file.close()
	for linha in leitor:
		if linha[0] == escolha:
			linha[1] = str(int(linha[1])+1)
			break
	file = open('turno1', 'w', encoding = 'utf8')
	escritor = csv.writer(file)
	escritor.writerows(leitor)
	file.close()

def monta_combinacoes():
	""" monta todas as combinações possíveis para um segundo turno e retorna em uma lista """
	combinacoes = []
	for i in range(len(candidatos)-2):
		for j in range(i+1, len(candidatos)-1):
			lista = [candidatos[i],candidatos[j]]
			combinacoes.append(lista)
	return combinacoes

def escolhasT2(escolhas):
	file = open('turno2', 'r', encoding = 'utf8')
	leitor = csv.reader(file)
	leitor = list(leitor)
	while [] in leitor:
		leitor.remove([])
	file.close()
	for i in range(len(leitor)):
		linha = leitor[i]
		c1 = linha[0]
		c2 = linha[2]
		if c1 == escolhas[i]:
			linha[1] = str(int(linha[1])+1)
		elif c2 == escolhas[i]:
			linha[3] = str(int(linha[3])+1)
		else:
			linha[5] = str(int(linha[5])+1)
	file = open('turno2', 'w', encoding = 'utf8')
	escritor = csv.writer(file)
	escritor.writerows(leitor)
	file.close()

def importaresultados():
	file = open('turno1', 'r', encoding = 'utf8')
	leitor = csv.reader(file)
	lista1 = list(leitor)
	file.close()
	file = open('turno2', 'r', encoding = 'utf8')
	leitor = csv.reader(file)
	lista2 = list(leitor)
	file.close()
	return(lista1,lista2)

def cria_turno1():
	matriz = []
	for candidato in candidatos:
		linha = [candidato,'0']
		matriz.append(linha)
	file = open('turno1', 'w', encoding = 'utf8')
	escritor = csv.writer(file)
	escritor.writerows(matriz)
	file.close()
def cria_turno2():
	matriz = monta_combinacoes()
	for linha in matriz:
		linha.insert(1,'0')
		linha.insert(3,'0')
		linha.append(candidatos[-1])
		linha.append('0')
	print(matriz)
	file = open('turno2', 'w', encoding = 'utf8')
	escritor = csv.writer(file)
	escritor.writerows(matriz)
	file.close()
# print(valida_cpf('367.752.028-22'))
# escolhaT1('Lula')
# print(monta_combinacoes())
# cria_turno2()