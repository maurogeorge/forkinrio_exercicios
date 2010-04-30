# -*- encoding:utf8 -*-
# ta dando erro devido aos espaços
def string_inverso(frase):
	
	retorno = ''
	palavra = ''
	
	for c in frase:
		
		print c
		
		palavra = palavra + c
		
		if c == ' ':
			retorno = retorno + palavra[::-1]
			palavra = ''
	
	return retorno
	
print string_inverso(u'Domingo de manhã e eu programando!')	