import re


def validar_letras(nome):
    if re.fullmatch(r"^[a-zA-Z]+$", nome):
        return True
    else:
        return False

condicao = True

while condicao:

    nome = input("Qual é o seu nome?\n")

    if validar_letras(nome):
        condicao = False
    else:
        print("Digite apenas letras, sem números ou caracteres especiais.")
