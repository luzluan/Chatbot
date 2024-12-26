import re


def validar_letras(nome):
    if re.fullmatch(r"^[a-zA-Z]+$", nome):
        return True
    else:
        return False


def corrige_valor_loop(condicao):
    if condicao:
        return False
    else:
        return True


condicao = True

while condicao:
    nome = input("Qual é o seu nome?\n")

    retorno_do_regex = validar_letras(nome)

    print("O Nome está devidamente validado? ", retorno_do_regex)

    condicao = corrige_valor_loop(retorno_do_regex)

    # condicao = False
