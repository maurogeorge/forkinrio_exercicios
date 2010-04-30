# -*- coding: utf8 -*-
# faltou a variação
def soma_media_variacao(dicionario):
	
	soma = 0
	
	for valor in dicionario.values():
		soma = soma + valor
		
	media = soma / len( dicionario.values() )	

	return u'A soma é igual a %.1f, media é igual a %.1f' %(soma, media) 
	
print soma_media_variacao({'a':30,'b':25, 'c':20})