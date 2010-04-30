# -*- coding: utf8 -*-"

"""
1. Implementar um gerador de números primos
"""
def gen_primos():
	
	num = 1
    
	while True:
		num += 1
		
		# 2 é primo
		if num == 2:
			yield num
		
		# remove os pares	
		if num % 2 == 0:	
			continue

		# Verifica se é divisivel por outro
		for i in range (3, num):
			if num % i == 0:
				break
		# Sem o else do for seria necessário
		# break para não repetir números
		# http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
		else:
			yield num
			
   		

# executa um exemplo		
for numeros in gen_primos():
	print numeros