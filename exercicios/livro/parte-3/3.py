# -*- coding: utf8 -*-

"""
3. Implementar um gerador que produza tuplas com as cores do padrão RGB
(R, G e B variam de 0 a 255) usando xrange() e uma função que produza uma
lista com as tuplas RGB usando range(). Compare a performance
"""

# gerador utilizando range
def gen_rgb_range():
	
	r = 0
	g = 0
	b = 0
	
	for i in range(256):
		r = i

		for j in range(256):
			g = j

			for k in range(256):
				b = k

				yield (r, g, b)

	

def gen_rgb_xrange():

		r = 0
		g = 0
		b = 0

		for i in xrange(256):
			r = i

			for j in xrange(256):
				g = j

				for k in xrange(256):
					b = k

					yield (r, g, b)
					


# executa um exemplo
for rgb in gen_rgb_xrange():
	print rgb	