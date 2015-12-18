#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
    # Abro o arquivo filename
    with open(filename) as arquivo:
        dicionario = {}

        # Recebo o texto do arquivo como uma string gigante e transformo em uma lista com o split
        # Dica do amigo de curso Adriano Regis me poupou fazer um laço for para retirar os \n
        palavras = arquivo.read().split()

        # Monto o dicionário
        for i in range(len(palavras) - 1):
            # Criamos uma lista para receber a palavra a frente
            lista = [palavras[i + 1]]
            # Se a palavra existe na chave do dicionario
            if palavras[i] in dicionario.keys():
                # Somente acrescento
                dicionario[palavras[i]] += lista
            else:
                # Senão uma nova é criada
                dicionario[palavras[i]] = lista
    return dicionario

def print_mimic(mimic_dict, word):
    # Cria uma lista para receber as chaves do dicionario
    lista = []
    lista += mimic_dict.keys()
    # Itero a randomização 200 vezes
    for i in range(200):
        # Se a palavra está no dicionário, escolha aleatoriamente dentro da lista e imprima
        if word in mimic_dict.keys():
            proxima = random.choice(mimic_dict[word])
            print(proxima, end=' ')
        # Senão, escolha aleatoriamente uma KEY e chame aleatoriamente uma palavra
        else:
            proxima = random.choice(mimic_dict[random.choice(lista)])
            print(proxima, end=' ')
    return

# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
