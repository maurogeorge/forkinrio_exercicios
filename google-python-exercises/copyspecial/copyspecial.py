#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


# fonte: http://code.google.com/intl/pt-BR/edu/languages/google-python-class/utilities.html
def get_special_paths(dir):

  retorno = []

  paths = os.listdir(dir)  # lista os arquivos do diretorio

  for arquivo in paths:
	
    match = re.search(r'__(\w+)__', arquivo)

    if match:
      retorno.append(os.path.abspath(os.path.join(dir, arquivo)))
  
  return retorno

print get_special_paths('./')



def copy_to(paths, dir):

  if not os.path.exists(dir):
    os.mkdir(dir)

  for path in paths:
    arquivo = os.path.basename(path)
    shutil.copy(path, os.path.join(dir, arquivo))


copy_to(get_special_paths('./'),'tmp')


def zip_to(paths, zipfile):
  # comando para criar o zip
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Zipando com:" + cmd
  (status, output) = commands.getstatusoutput(cmd)

  if status:
    sys.stderr.write(output)
    sys.exit(1)

zip_to(get_special_paths('./'), 'zip')


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
