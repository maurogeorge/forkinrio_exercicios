# -*- coding: utf8 -*-"

"""
2. Crie uma classe derivada de lista
com um método retorne os elementos da lista
sem repetição

>>> Lista([1,2,2,3]) - [3,4,5,6]
[1, 2, 3, 4, 5, 6]
"""

class Lista(list):
	
	def __sub__(self, l):
		
		retorno = []
		
		soma = self + l
		
		for i in soma:
			if i not in retorno:
				retorno.append(i)
		
		return retorno			
	

if __name__ == "__main__":
	import doctest
	doctest.testmod()