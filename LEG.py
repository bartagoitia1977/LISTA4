###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-11-17
#
# Descricao:  GRAFO LISTA4 Q1 - LISTA ENCADEADA
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

class No:
	'''
	NO VAZIO DA LISTA ENCADEADA
	'''
	def __init__(self,objeto = None,proximo = None,indice = 0):
		self._objeto = objeto
		self._proximo = proximo
		self._indice = indice

	@property
	def proximo(self):
		return self._proximo

	@proximo.setter
	def proximo(self,item):
		self._proximo = item

	@property
	def objeto(self):
		return self._objeto

	@objeto.setter
	def objeto(self,item):
		self._objeto = item

	@property
	def indice(self):
		return self._indice

	@indice.setter
	def indice(self,item):
		self._indice = item	

	def __repr__(self):
		if (type(self.objeto) == str):
			self.objetostring = "'"+str(self.objeto)+"'"
		else:
			self.objetostring = str(self.objeto)
		return self.objetostring

class Ponteiro:
	def __init__(self,lista):
		self._ptr = lista.cabeca

	def __next__(self):
		if self._ptr.proximo is None:
			raise StopIteration
		else:
			self._ptr = self._ptr.proximo
			return self._ptr.objeto

class LE:
	'''
	LISTA ENCADEADA SIMPLES (APENAS FUNCOES QUE SERÃO UTILIZADAS)
	'''
	def __init__(self):
		self._cabeca = self._fim = No()

	@property
	def cabeca(self):
		return self._cabeca
		

	def anexar(self,item):
		self._item = item
		self._novono = No(self._item,None,0)
		index = 0
		aux = self._cabeca.proximo
		if (aux is None):
			self._cabeca.proximo = self._novono
			self._fim = self._novono
		else:
			while not(aux is None):
				aux = aux.proximo
				index += 1
			self._novono.indice = index
			self._fim.proximo = self._novono
			self._fim = self._novono

	def deletar(self,indice):
		self._indice = indice
		aux1 = self._cabeca
		aux2 = self._cabeca.proximo
		stop = 0
		if (aux2 is None):
			raise KeyError
		else:
			while not(aux2 is None) and (stop == 0):
				if (self._indice == aux2.indice):
					aux1.proximo = aux2.proximo
					if (aux2 == self._fim):
						self._fim = aux1
					stop = 1
				else:
					aux1 = aux1.proximo
					aux2 = aux2.proximo
			if (stop == 0):
				raise KeyError
			else:
				aux3 = aux2.proximo
				while not(aux3 is None):
					aux3.indice -= 1
					aux3 = aux3.proximo
				return aux2.objeto
				del aux2

	def __str__(self):
		self._LEstring = "["
		aux = self._cabeca.proximo
		if (aux is None):
			self._LEstring = self._LEstring+"]"
			return self._LEstring
		else:
			while not(aux is None):
				self._LEstring += str(aux)+" # "
				aux = aux.proximo
			self._LEstring = self._LEstring[:-3]+"]"
			return self._LEstring

	def __repr__(self):
		return self.__str__()

	def __getitem__(self,item):
		self.__item = item
		finder = self._cabeca.proximo
		if (finder is None):
			raise IndexError
		else:
			while not(finder is None) and (finder.indice != self.__item):
				finder = finder.proximo
			if (finder is None):
				raise IndexError 
			else:
				if (finder.indice == self.__item):
					return finder.objeto

	def __iter__(self):
		return Ponteiro(self)

	def __len__(self):
		aux = self._fim
		if (self._fim == self._cabeca):
			return self._fim.indice
		else:
			return (self._fim.indice + 1)