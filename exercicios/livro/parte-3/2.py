# -*- coding: utf8 -*-

"""
2. Implementar o gerador de numeros primos como uma expressão
(dica: use o modulo itertools).
"""

import itertools

def primo(num):

	for i in range (3, num):
		if num % i == 0:
			return False
	else:
		return True
		

# O ifilter irá retornar apenas os valores True avaliando a função primo, em seguida
# verifica se é o 2 ou se é impar, o count do itertools conta a partir do número + 1
iteravel = itertools.ifilter( primo, itertools.ifilter( lambda  x: x == 2 or x % 2, itertools.count(2) ) )

# executa um exemplo
for x in iteravel:
	print x