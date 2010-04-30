# -*- coding: utf8 -*-

"""
4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas com os dados
o separador de campo do arquivo é virgula, eliminando as linhas vazias. Caso ocorra algum problema,
imprima uma mensagem de aviso e encerre o programa.
"""

def gen_arquivo(arquivo):
	
	arquivo = open(arquivo, 'r')
	conteudo = arquivo.read()
	

	
	# http://docs.python.org/library/stdtypes.html#str.split
	for i in conteudo.split(','):
		
		# Tupla de apenas um elemento colocar uma virgula
		# strip(), remove os espaços em branco
		
		
		yield ( i.strip(),)


print 'mississ\n\nippis'.splitlines()

try:
	
	for palavra in gen_arquivo('4_arquivo.txt'):
		print palavra
	
except Exception as e:
        print e

