###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-11-19
#
# Descricao:  GRAFO LISTA4 Q1
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

###############################################################################
# QUESTÃO 2
# A implemantação de um grafo com representacao matricial possui busca mais
# rapida, em compensacao ele consome mais memoria. Aconselhavel para grafos 
# pequenos.
# A implementacao em lista representa economia de memoria, em compensacao
# sua busca e um pouco mais demorada. Aconselhavel para grafos maiores.
# O ideal seria uma representacao que fosse mista (Matriz X Lista)
###############################################################################

import numpy as np
from LEG import No
from LEG import LE

class GrafoMatriz:
	'''
	Parametros: lista ou vetor de tuplas: (vertice1,vertice2) indicando as arestas do grafo;
	(vertice1,vertice2,peso)quando as arestas têm peso;
	somente lista de vertices: grafo nao direcionado; lista de vertices, 'True': grafo direcionado.
	'''
	def __init__(self,vetor_tuplas,direcao = False):
		self._direcao = direcao
		self._vetor_tuplas = vetor_tuplas
		if (len(self._vetor_tuplas[0]) > 2):
			self._peso = True
		else:
			self._peso = False
		self._lista_numeros = np.array([],dtype = np.int8)
		self._lista_pesos = np.array([],dtype = np.int8)
		self._arestas = len(self._vetor_tuplas)
		for tupla in self._vetor_tuplas:
			self._conttupla = 0
			for t in tupla:
				if (self._conttupla <= 1):
					self._lista_numeros = np.append(self._lista_numeros,t)
					self._conttupla += 1
				else:
					self._lista_pesos = np.append(self._lista_pesos,t)
		self._vertices = max(self._lista_numeros) + 1
		self._tuplavertices = (int(self._vertices),(int(self._vertices)))
		self._matriz_grafo = np.zeros(self._tuplavertices,dtype = np.int8)
		self._count = 0
		for tupla in self._vetor_tuplas:
			if (self._peso == True):
				self._matriz_grafo[tupla[0]][tupla[1]] = self._lista_pesos[self._count]
				if (self._direcao == False):
					self._matriz_grafo[tupla[1]][tupla[0]] = self._lista_pesos[self._count]
				self._count += 1
			else:
				self._matriz_grafo[tupla[0]][tupla[1]] = 1
				if (self._direcao == False):
					self._matriz_grafo[tupla[1]][tupla[0]] = 1

	def __repr__(self):
		self._grafo_string = "["
		for linha in self._matriz_grafo:
			self._grafo_string += "["
			for num in linha:
				self._grafo_string += str(num) +","
			self._grafo_string = self._grafo_string[:-1]
			self._grafo_string += "],"
		self._grafo_string = self._grafo_string[:-1]
		self._grafo_string += "]"
		return self._grafo_string
		
	def __str__(self):
		return self.__repr__()

	def __getitem__(self,item):
		self._item = item
		self._minilista = []
		self._ct = 0
		for n in self._matriz_grafo[self._item]:
			if (n != 0):
				if (self._peso == False):
					self._minilista.append((self._item,self._ct))
				else:
					self._minilista.append((self._item,self._ct,n))
			self._ct += 1
		return self._minilista

	def VE(self):
		'''
		Retorna tupla: (vertices,arestas)
		'''
		self._tupla_tamanho = (self._vertices,self._arestas)
		return self._tupla_tamanho

	def existeAresta(self,num1,num2):
		'''
		Dada uma aresta retorna: True - existente; False - nao existente.
		'''
		self._num1 = num1
		self._num2 = num2
		self._conteudo_grafo2 = 0
		if ((self._num1 >= len(self._matriz_grafo)) or (self._num2 >= len(self._matriz_grafo))):
			return False
		else:
			if (self._direcao == True):
				self._conteudo_grafo = self._matriz_grafo[self._num1][self._num2]
				if (self._conteudo_grafo != 0):
					return True
				else:
					return False
			else:
				self._conteudo_grafo = self._matriz_grafo[self._num1][self._num2]
				self._conteudo_grafo2 = self._matriz_grafo[self._num2][self._num1]
				if ((self._conteudo_grafo != 0) or (self._conteudo_grafo2 != 0)):
					return True
				else:
					return False

	def grauSaida(self,vertice):
		'''
		Parametro: vertice - retorna grau de saida num grafo direcionado.
		'''
		self._vertice = vertice
		if (self._direcao == False):
			print("Grafo nao direcionado!")
		else:
			self._subvetor = self._matriz_grafo[self._vertice]
			self._cont = 0
			for i in self._subvetor:
				if (i != 0):
					self._cont += 1
			return self._cont

	def grauEntrada(self,vertice):
		'''
		Parametro: vertice - retorna grau de entrada num grafo direcionado.
		'''
		self._vertice = vertice
		if (self._direcao == False):
			print("Grafo nao direcionado!")
		else:
			self._cont = 0
			for v in self._matriz_grafo:
				if (v[self._vertice] != 0):
					self._cont += 1
			return self._cont

	def tree(self):
		'''
		Retorna True se for arvore ou False se nao for arvore.
		'''
		if (self._arestas == (self._vertices - 1)):
			return True
		else:
			return False
		

	def removeVertice(self,vertice):
		'''
		Dado um vertice remove todas as arestas ligadas a ele.
		'''
		self._vertice = vertice
		self._cont_arestas_removidas = 0
		for a in range(len(self._matriz_grafo)):
			if (self._matriz_grafo[a][self._vertice] != 0):
				self._matriz_grafo[a][self._vertice] = 0
				self._cont_arestas_removidas += 1
		for b in range(len(self._matriz_grafo)):
			if (self._matriz_grafo[self._vertice][b] != 0):
				self._matriz_grafo[self._vertice][b] = 0
				self._cont_arestas_removidas += 1
		if (self._direcao == False):
			self._arestas -= (self._cont_arestas_removidas // 2)
		else:
			self._arestas -= self._cont_arestas_removidas
		self._vertices -= 1

	def removeAresta(self,num1,num2):
		'''
		Dada uma aresta remove a aresta.
		'''
		self._num1 = num1
		self._num2 = num2
		if (self.existeAresta(self._num1,self._num2) == True):
			self._cont_arestas_removidas = 0
			self._matriz_grafo[self._num1][self._num2] = 0
			self._cont_arestas_removidas += 1
			if (self._direcao == False):
				self._matriz_grafo[self._num2][self._num1] = 0
			self._arestas -= self._cont_arestas_removidas
		else:
			print("Aresta inexistente")

	def adicionaAresta(self,num1,num2,peso = None):
		'''
		Dados dois numeros: adiciona aresta; se numero for maior que numero de vertices, adiciona
		mais um vertice e a aresta. Se houver peso adiciona peso (3o. parametro).
		'''
		self._num1 = num1
		self._num2 = num2
		self._pesodado = peso
		if (self.existeAresta(self._num1,self._num2) == True):
			print("Aresta ja existe!")
		else:
			if ((self._num1 >= len(self._matriz_grafo)) or (self._num2 >= len(self._matriz_grafo))):
				self._matriz_auxiliar = np.zeros((int(self._vertices) + 1, int(self._vertices) + 1),dtype = np.int8)
				for m in range(len(self._matriz_grafo)):
					for n in range(len(self._matriz_grafo)):
						self._matriz_auxiliar[m][n] = self._matriz_grafo[m][n]
				if (self._direcao == False):
					if (self._peso == True):
						self._matriz_auxiliar[self._num1][self._num2] = self._pesodado
						self._matriz_auxiliar[self._num2][self._num1] = self._pesodado
					else:
						self._matriz_auxiliar[self._num1][self._num2] = 1
						self._matriz_auxiliar[self._num2][self._num1] = 1
				else:
					if (self._peso == True):
						self._matriz_auxiliar[self._num1][self._num2] = self._pesodado
					else:
						self._matriz_auxiliar[self._num1][self._num2] = 1
				self._vertices += 1
				self._arestas += 1
				self._matriz_grafo = self._matriz_auxiliar
			else:
				if (self._direcao == False):
					if (self._peso == True):
						self._matriz_grafo[self._num1][self._num2] = self._pesodado
						self._matriz_grafo[self._num2][self._num1] = self._pesodado
					else:
						self._matriz_grafo[self._num1][self._num2] = 1
						self._matriz_grafo[self._num2][self._num1] = 1
				else:
					if (self._peso == True):
						self._matriz_grafo[self._num1][self._num2] = self._pesodado
					else:
						self._matriz_grafo[self._num1][self._num2] = 1
				self._arestas += 1

	def MatrizLista(self):
		self._listatuplas = []
		if (self._peso == False):
			self._countm = 0
			for m in self._matriz_grafo:
				self._countn = 0
				for n in m:
					if (n != 0):
						self._tupla = (self._countm,self._countn)
						print(self._tupla)
						self._listatuplas.append(self._tupla)
						self._countn += 1
					else:
						self._countn += 1
				self._countm += 1
		else:
			self._countm = 0
			for m in self._matriz_grafo:
				self._countn = 0
				for n in m:
					if (n != 0):
						self._tupla = (self._countm,self._countn,n)
						print(self._tupla)
						self._listatuplas.append(self._tupla)
						self._countn += 1
					else:
						self._countn += 1
				self._countm += 1
		self._grafoLista = GrafoLista(self._listatuplas,self._direcao)
		return self._grafoLista

class GrafoLista:
	'''
	Parametros: lista ou vetor de tuplas: (vertice1,vertice2) indicando as arestas do grafo;
	(vertice1,vertice2,peso)quando as arestas têm peso;
	somente lista de vertices: grafo nao direcionado; lista de vertices, 'True': grafo direcionado.
	'''
	def __init__(self,vetor_tuplas,direcao = False):
		self._direcao = direcao
		self._vetor_tuplas = vetor_tuplas
		if (len(self._vetor_tuplas[0]) > 2):
			self._peso = True
		else:
			self._peso = False
		self._listabase = LE()
		self._lista_numeros = np.array([],dtype = np.int8)
		self._lista_pesos = np.array([],dtype = np.int8)
		self._arestas = len(self._vetor_tuplas)
		for tupla in self._vetor_tuplas:
			self._conttupla = 0
			for t in tupla:
				if (self._conttupla <= 1):
					self._lista_numeros = np.append(self._lista_numeros,t)
					self._conttupla += 1
				else:
					self._lista_pesos = np.append(self._lista_pesos,t)
		self._vertices = max(self._lista_numeros) + 1
		for n in range(self._vertices):
			self._sublista = LE()
			self._listabase.anexar(self._sublista)
		self._count = 0
		for tupla in self._vetor_tuplas:
			if (self._peso == True):
				self._listabase[tupla[0]].anexar((tupla[1],self._lista_pesos[self._count]))
				if (self._direcao == False):
					self._listabase[tupla[1]].anexar((tupla[0],self._lista_pesos[self._count]))
				self._count += 1
			else:
				self._listabase[tupla[0]].anexar(tupla[1])
				if (self._direcao == False):
					self._listabase[tupla[1]].anexar(tupla[0])

	
	def __repr__(self):
		self._grafo_string = str(self._listabase)
		return self._grafo_string
		
	def __str__(self):
		return self.__repr__()

	def __getitem__(self,item):
		self._item = item
		self._minilista = []
		self._listaprocura = self._listabase[self._item]
		for n in self._listaprocura:
			if (self._peso == False):
				self._minilista.append((self._item,n))
			else:
				self._minilista.append((self._item,n[0],n[1]))
		return self._minilista
		

	def VE(self):
		'''
		Retorna tupla: (vertices,arestas)
		'''
		self._tupla_tamanho = (self._vertices,self._arestas)
		return self._tupla_tamanho

	def existeAresta(self,num1,num2):
		'''
		Dada uma aresta retorna: True - existente; False - nao existente.
		'''
		self._num1 = num1
		self._num2 = num2
		if ((self._num1 >= len(self._listabase)) or (self._num2 >= len(self._listabase))):
			return False
		else:
			if (self._peso == False):
				self._comp1 = False
				self._comp2 = False
				if (self._direcao == True):
					self._listaprocura = self._listabase[self._num1]
					if (len(self._listaprocura) == 0):
						return False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x == self._num2):
								return True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							return False
				else:
					self._listaprocura = self._listabase[self._num1]
					if (len(self._listaprocura) == 0):
						self._comp1 = False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x == self._num2):
								self._comp1 = True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							self._comp1 = False

					self._listaprocura = self._listabase[self._num2]
					if (len(self._listaprocura) == 0):
						self._comp2 = False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x == self._num1):
								self._comp2 = True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							self._comp2 = False
					if (self._comp1 or self._comp2):
						return True
					else:
						return False
			else:
				self._comp1 = False
				self._comp2 = False
				if (self._direcao == True):
					self._listaprocura = self._listabase[self._num1]
					if (len(self._listaprocura) == 0):
						return False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x[0] == self._num2):
								return True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							return False
				else:
					self._listaprocura = self._listabase[self._num1]
					if (len(self._listaprocura) == 0):
						self._comp1 = False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x[0] == self._num2):
								self._comp1 = True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							self._comp1 = False

					self._listaprocura = self._listabase[self._num2]
					if (len(self._listaprocura) == 0):
						self._comp2 = False
					else:
						for x in self._listaprocura:
							self._cont = 0
							if (x[0] == self._num1):
								self._comp2 = True
								break
							else:
								self._cont += 1
						if (self._cont > 0):
							self._comp2 = False
					if (self._comp1 or self._comp2):
						return True
					else:
						return False

	def grauSaida(self,vertice):
		'''
		Parametro: vertice - retorna grau de saida num grafo direcionado.
		'''
		self._vertice = vertice
		if (self._direcao == False):
			print("Grafo nao direcionado!")
		else:
			self._subvetor = self._listabase[self._vertice]
			self._cont = len(self._subvetor)
			return self._cont

	def grauEntrada(self,vertice):
		'''
		Parametro: vertice - retorna grau de entrada num grafo direcionado.
		'''
		self._vertice = vertice
		if (self._direcao == False):
			print("Grafo nao direcionado!")
		else:
			self._count = 0
			for l in self._listabase:
				self._subvetor = l
				for x in self._subvetor:
					if (self._peso == False):
						if (x == self._vertice):
							self._count += 1
					else:
						if (x[0] == self._vertice):
							self._count += 1
			return self._count

	def tree(self):
		'''
		Retorna True se for arvore ou False se nao for arvore.
		'''
		if (self._arestas == (self._vertices - 1)):
			return True
		else:
			return False

	def removeVertice(self,vertice):
		'''
		Dado um vertice remove todas as arestas ligadas a ele.
		'''
		self._vertice = vertice
		self._subvetor = self._listabase[self._vertice]
		self._cont_arestas_removidas = 0
		for a in range(len(self._listabase[self._vertice])):
			self._listabase[self._vertice].deletar(0)
			self._cont_arestas_removidas +=1		
		self._ct1 = 0
		for l in self._listabase:
			self._ct2 = 0
			for x in l:
				print(x)
				print(self._ct1)
				print(self._ct2)
				if (self._peso == False):
					if (x == self._vertice):
						self._listabase[self._ct1].deletar(self._ct2)
						self._cont_arestas_removidas += 1
					else:
						self._ct2 += 1
				else:
					if (x[0] == self._vertice):
						self._listabase[self._ct1].deletar(self._ct2)
						self._cont_arestas_removidas += 1
					else:
						self._ct2 += 1
			self._ct1 += 1				
		if (self._direcao == False):
			self._arestas -= (self._cont_arestas_removidas // 2)
		else:
			self._arestas -= self._cont_arestas_removidas
		self._vertices -= 1

	def removeAresta(self,num1,num2):
		'''
		Dada uma aresta remove a aresta.
		'''
		self._num1 = num1
		self._num2 = num2
		if (self.existeAresta(self._num1,self._num2) == True):
			self._cont_arestas_removidas = 0
			self._ct = 0
			for a in self._listabase[self._num1]:
				if (a == self._num2):
					self._listabase[self._num1].deletar(self._ct)
					self._cont_arestas_removidas += 1
					break
				else:
					self._ct += 1
			if (self._direcao == False):
				self._ct = 0
				for a in self._listabase[self._num2]:
					if (a == self._num1):
						self._listabase[self._num2].deletar(self._ct)
						break
					else:
						self._ct += 1
			self._arestas -= self._cont_arestas_removidas
		else:
			print("Aresta inexistente")

	
	def adicionaAresta(self,num1,num2,peso = None):
		'''
		Dados dois numeros: adiciona aresta; se numero for maior que numero de vertices, adiciona
		mais um vertice e a aresta. Se houver peso adiciona peso (3o. parametro).
		'''
		self._num1 = num1
		self._num2 = num2
		self._pesodado = peso
		if (self.existeAresta(self._num1,self._num2) == True):
			print("Aresta ja existe!")
		else:
			if ((self._num1 >= self.VE()[0]) or (self._num2 >= self.VE()[0])):
				self._listabase_auxiliar = LE()
				for n in range(self._vertices + 1):
					self._sublista = LE()
					self._listabase_auxiliar.anexar(self._sublista)
				for l in range(len(self._listabase)):
					for v in range(len(self._listabase[l])):
						self._listabase_auxiliar[l].anexar(self._listabase[l][v])
				if (self._direcao == False):
					if (self._peso == True):
						self._tuplapeso = (self._num2,self._pesodado)
						self._listabase_auxiliar[self._num1].anexar(self._tuplapeso)
						self._tuplapeso = (self._num1,self._pesodado)
						self._listabase_auxiliar[self._num2].anexar(self._tuplapeso)
					else:
						self._listabase_auxiliar[self._num1].anexar(self._num2)
						self._listabase_auxiliar[self._num2].anexar(self._num1)
				else:
					if (self._peso == True):
						self._tuplapeso = (self._num2,self._pesodado)
						self._listabase_auxiliar[self._num1].anexar(self._tuplapeso)
					else:
						self._listabase_auxiliar[self._num1].anexar(self._num2)
				self._vertices += 1
				self._arestas += 1
				self._listabase = self._listabase_auxiliar
			else:
				if (self._direcao == False):
					if (self._peso == True):
						self._tuplapeso = (self._num2,self._pesodado)
						self._listabase[self._num1].anexar(self._tuplapeso)
						self._tuplapeso = (self._num1,self._pesodado)
						self._listabase[self._num2].anexar(self._tuplapeso)
					else:
						self._listabase[self._num1].anexar(self._num2)
						self._listabase[self._num2].anexar(self._num1)
				else:
					if (self._peso == True):
						self._tuplapeso = (self._num2,self._pesodado)
						self._listabase[self._num1].anexar(self._tuplapeso)
					else:
						self._listabase[self._num1].anexar(self._num2)
				self._arestas += 1	

	def ListaMatriz(self):
		self._listatuplas = []
		if (self._peso == False):
			self._countm = 0
			for m in self._listabase:
				for n in m:
					self._tupla = (self._countm,n)
					self._listatuplas.append(self._tupla)
				self._countm += 1					
		else:
			self._countm = 0
			for m in self._listabase:
				for n in m:
					self._tupla = (self._countm,n[0],n[1])
					self._listatuplas.append(self._tupla)
				self._countm += 1
		self._grafoMatriz = GrafoMatriz(self._listatuplas,self._direcao)
		return self._grafoMatriz