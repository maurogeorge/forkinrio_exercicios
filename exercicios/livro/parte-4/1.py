# -*- coding: utf8 -*-"

"""
1. Crie uma classe que modele um quadrado
com um atributo lado e os métodos: mudar valor do lado,
retornar valor do lado e calcular área.
"""

class Quadrado(object):
	
	
	def setLado(self, lado):
		self.lado = lado
	
	def getLado(self):
		return self.lado
		
	def area(self):
		return self.lado**2	
	

# Executando	
quadrado = Quadrado()
quadrado.setLado(7)
print quadrado.getLado()
print quadrado.area()