# -*- coding: utf8 -*-

"""
1. Implementar uma função que formate uma lista de tuplas como
tabela HTML
"""

def tabela_html(lista):
	
	# Cria a tabela
	retorno = '<table> \n'
	
	# Cada tupla na lista representa uma linha
	for tupla in lista:
		# Cria a linha
		retorno += '\t <tr> \n'
		
		# lê os dados da tupla	
		for dado in tupla:
			retorno += '\t \t<td>%s</td>\n' %(dado)
			
		# Termina a linha
		retorno += '\t</tr>\n'	

	# Finaliza a tabela
	retorno += '</table>'
	
	# Grava os dados em arquivo.html
	arquivo = file('arquivo.html', 'w')
	arquivo.write(retorno)

	
# Executando
lista = [('Header 1', 'Header 2', 'Header 3'), ('dado 1', 'dado 2', 'dado 3'), ('dado 4', 'dado 5', 'dado 6')]
tabela_html(lista)	