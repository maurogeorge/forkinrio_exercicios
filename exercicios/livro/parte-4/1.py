# -*- coding: utf8 -*-"

"""
1. Crie uma classe que modele um quadrado
com um atributo lado e os métodos: mudar valor do lado,
retornar valor do lado e calcular área.

>>> quadrado = Quadrado()
>>> quadrado.set_lado(7)
>>> quadrado.lado
7

>>> quadrado.get_lado()
7

>>> quadrado.area()
49
"""

class Quadrado(object):
	
	
	def set_lado(self, lado):
		self.lado = lado
	
	def get_lado(self):
		return self.lado
		
	def area(self):
		return self.lado**2	
	


if __name__ == "__main__":
	import doctest
	doctest.testmod()