from random import sample, choice
from string import ascii_lowercase, ascii_uppercase, digits


def gera_senha(tamanho: int = 6) -> str:
    minusculas = ascii_lowercase
    maiusculas = ascii_uppercase
    numeros = digits
    simbolos = '!%$#@*&'
    todos = minusculas + maiusculas + numeros + simbolos
    senha = ''
    g = sample(todos, tamanho)
    senha = ''.join(g)

    return senha