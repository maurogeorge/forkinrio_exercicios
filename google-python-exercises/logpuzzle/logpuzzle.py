#!/usr/bin/python
# _*_ encoding: utf8 _*_
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

"""
Utilizada para ordenar o puzzle do place
sorted aceita paramêtros extras em http://docs.python.org/library/functions.html#sorted
se casar com a expressão ordenara pelo segundo paramêtro senão retorna a url normal
assim funcionando no animal e no place
"""
def ordena_place(url):
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  #Extraindo o hostname
  underline = filename.find('_')
  hostname = filename[underline + 1:]

  file = open(filename)
  
  url_dict = {}

  for line in file:
	# Apos o GET casa com os caracteres sem espaço
    match = re.search(r'"GET (\S+)', line)
		
    if match:
	  # Os caracteres sem espaço	
      path = match.group(1)
	  
      if 'puzzle' in path:
        # Armazena na chave do dicionario
		url_dict['http://' + hostname + path] = 1
	
  # Utilizo a função criada anteriormente para definir a ordem
  # de ordenação da chave	
  return sorted(url_dict.keys(), key=ordena_place)

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  # Cria o diretorio de destino se não existir
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  # Abrindo o arquivo para escrita, path.join une os paths inteligentemente
  # write escreve no arquivo
  index = open(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')
  
  # contador para dar o nome as imagens
  i = 0

  # Loop para recuperar as imagens
  for img_url in img_urls:
	
	# Dando o nome as imagens
    img_nome = 'img%d' %( i )

    # Só pra ter algo na tela enquanto baixa
    print 'Baixando...', img_url

    # Baixa a imagem da url e coloca no diretorio de destino com o nome criado
    urllib.urlretrieve(img_url, os.path.join(dest_dir, img_nome))

    # Escreve no index o nome da imagem
    index.write('<img src="%s">' % (img_nome))

    # Incrementa o contador
    i += 1

  # Ao sair do for termina o HTML
  index.write('\n</body></html>\n')
  # Fecha o arquivo
  index.close()

# Executando
# recuperando as urls ordenadas
print read_urls('animal_code.google.com')
# Baixando os arquivos
download_images(read_urls('animal_code.google.com'), 'img')

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
