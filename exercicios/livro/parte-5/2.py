# -*- coding: utf8 -*-

"""
2. Implementar uma função que formate uma lista de tuplas como
tabela HTML
"""

def tabela_html(lista):
	
	# Cria a tabela
	retorno = '<table> \n'
	
	# Cria o head da tabela
	retorno += '\t<thead>\n'
	retorno += '\t\t<tr>\n'
	
	# lê a primeira tupla, e cria o head
	for dado in lista[0]:
		retorno += '\t\t\t<th>%s</th>\n' %(dado)
	
	# Finaliza o head	
	retorno += '\t\t</tr>\n'
	retorno += '\t</thead>\n'
	
	# Cria o corpo da tabela
	retorno += '\t<tbody>\n'
	
	# Cada tupla na lista representa uma linha começando da segunda pois a primeira é o head
	for tupla in lista[1:]:
		# Cria a linha
		retorno += '\t\t<tr> \n'
		
		# lê os dados da tupla	
		for dado in tupla:
			retorno += '\t\t\t<td>%s</td>\n' %(dado)
			
		# Termina a linha
		retorno += '\t\t</tr>\n'	

	# Finaliza a tabela
	retorno += '\t</tbody>\n'
	retorno += '</table>'
	
	# Grava os dados em arquivo.html
	arquivo = file('arquivo.html', 'w')
	arquivo.write(retorno)

	
# Executando
lista = [('Header 1', 'Header 2', 'Header 3'), ('dado 1', 'dado 2', 'dado 3'), ('dado 4', 'dado 5', 'dado 6')]
tabela_html(lista)	