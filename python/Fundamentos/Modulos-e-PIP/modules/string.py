'''
Inverter uma string de trás pra frente.

Retornar apenas letras com índice par.

Retornar apenas letras com índice ímpar.
'''

def invert_string (word):
    return word[::-1]

def word_par (word):
    return word[::2]

def word_impar(word):
    return word[1::2]