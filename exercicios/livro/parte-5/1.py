# -*- coding: utf8 -*-

"""
1. Implementar uma classe Animal com os atributos
nome, espécie, genêro, peso, altura e idade. O objeto derivado desta classe
devera salvar seu estado em arquivo com o método "salvar" e recarregar o estado em
um método chamado "desfazer"
"""

import pickle

class Animal(object):
	
	def __init__(self, nome, especie, genero, peso, altura, idade):
		self.nome = nome
		self.especie = especie
		self.genero = genero
		self.peso = peso
		self.altura = altura
		self.idade  = idade
		
	def __repr__(self):
		# Representação em string dos dados
		return '%s, %s, %s, %.1f, %.1f, %d'%(self.nome, self.especie, self.genero, self.peso, self.altura, self.idade)
		
		
	def salvar(self):
		# Adicionando os dados ao dicionário		
		dados = {
			'nome': self.nome,
			'especie': self.especie,
			'genero': self.genero,
			'peso': self.peso,
			'altura': self.altura,
			'idade': self.idade
		}
		# Criando os arquivos com os dados		
		pickle.dump(dados, file('dados.pkl', 'w'))
	
		
	def desfazer(self):
		# Recuperando os dados
		dados = pickle.load(file('dados.pkl'))
		
		# Recarregando os dados
		self.nome = dados['nome']
		self.especie = dados['especie']
		self.genero = dados['genero']
		self.peso = dados['peso']
		self.altura = dados['altura']
		self.idade = dados['idade']
	
		
		
		
		
# executando
cachorro = Animal('Buddy', 'Labrador', 'Disney', 20, 0.7, 5)
cachorro.salvar()
cachorro.desfazer()
print cachorro

		
		
		
		



