# -*- coding: utf8 -*-"

"""
3. Implemente uma classe Carro com as seguintes propriedades:
- Um veículo tem um certo consumo de combustível(medidos em Km / litro)
  e uma certa quantidade de combustível no tanque
- O consumo é especificado no construtor e o nível inicial do combustivél é zero
- Forneça um método mover (km) que receba a distância em quilômetros e reduza o nivel de
  combustível no tanque de gasolina.
- Forneça um método gasolina que retorno o nivel atual de combustível.
- Forneça um método abastecer(litros), para abastecer o tanque
"""

class Carro(object):
	
	# Define o consumo em litros por 1Km
	def __init__(self, consumo):
		self.consumo = consumo
		self.combustivel = 0
	
	# Define o método mover	
	def mover(self,km):
		consumo = self.consumo * km
		self.combustivel -= consumo

	# Define o método gasolina		
	def gasolina(self):
		return self.combustivel
	
	# Define o método abastecer	
	def abastecer(self, combustivel):
		self.combustivel += combustivel


# Executando
carrinho = Carro(10)
carrinho.abastecer(100)
carrinho.mover(3)
print carrinho.gasolina()			
	