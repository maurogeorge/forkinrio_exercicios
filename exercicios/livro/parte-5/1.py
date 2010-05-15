# -*- coding: utf8 -*-

"""
1. Implementar uma classe Animal com os atributos
nome, espécie, genêro, peso, altura e idade. O objeto derivado desta classe
devera salvar seu estado em arquivo com o método "salvar" e recarregar o estado em
um método chamado "desfazer"
"""

import xml.dom.minidom

class Animal(object):
	
	def __init__(self, nome, especie, genero, peso, altura, idade):
		self.nome = nome
		self.especie = especie
		self.genero = genero
		self.peso = peso
		self.altura = altura
		self.idade  = idade
		
	def salvar(self):		
		# Cria o Documento XML
		documento = xml.dom.minidom.Document()
		
		# Criando os elementos
		root = documento.createElement('Animal')
		especie = documento.createElement(self.especie)
		genero = documento.createElement(self.genero)
		
		# Definindo os atributos do gênero
		genero.setAttribute('nome', self.nome)
		genero.setAttribute('peso', self.peso)
		genero.setAttribute('altura', self.altura)
		genero.setAttribute('idade', self.idade)
		
		# Montando o XML
		documento.appendChild(root)
		root.appendChild(especie)
		especie.appendChild(genero)
		
		# Cria um arquvio.xml com os dados
		arquivo = open('arquivo.xml','w')
		arquivo.write(documento.toprettyxml())
		
		
	def desfazer(self):
		documento = xml.dom.minidom.parse('arquivo.xml')	
		print documento
		
		
		

cachorro = Animal('Buddy', 'Labrador', 'Disney', '20', '0.7', '5')
cachorro.salvar()
cachorro.desfazer()	
		
		
		
		



