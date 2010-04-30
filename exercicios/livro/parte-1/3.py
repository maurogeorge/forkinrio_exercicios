def lista_de_listas(lista):

	retorno = []

	for item in lista:

		while item:
			retorno.append(item.pop(0))

	return retorno
	
print lista_de_listas([[1,2,3],[4,5,6]])	