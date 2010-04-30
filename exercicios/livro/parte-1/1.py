def celsius_para_fahrenheit(celsius):
	resultado = (9.0/5) * celsius + 32
	return resultado
	
def fahrenheit_para_celsius(fahrenheit):
	resultado = (fahrenheit - 32) / (9.0/5)	
	return resultado
	
print celsius_para_fahrenheit(20)
print fahrenheit_para_celsius(68)