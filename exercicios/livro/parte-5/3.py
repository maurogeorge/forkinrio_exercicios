# -*- coding: utf8 -*-

"""
3. Implementar uma aplicação web com uma
saudação dependente do horário(exemplos: "Bom dia são 9:00", "Boa tarde são 13:00" e
"Boa noite são 23:00")
"""

import cherrypy
import time

class Hora(object):

    def index(self):
        # Recupera a hora
		hora = "%d:%d" %(time.localtime()[3:5])
		
		if hora > '6:00' and hora <= '12:00':
			saudacao = 'Bom dia'
		elif hora > '12:00' and hora <= '18:00':
			saudacao = 'Boa tarde'
		else:
			saudacao = 'Boa noite'		
			
		
		return '%s, são %s.' % (saudacao,hora)
		
    index.exposed = True

cherrypy.quickstart(Hora())
