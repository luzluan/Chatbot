import re

print("Olá!\n - apresentação -")

def validar_nome(nome):
    if re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ' -]{2,}$", nome):
        return True
    else:
        return False

def confirmar(user_input):
    resposta = ['sim', 's', 'yes', 'y', 'correto']
    return user_input.strip().lower() in resposta

condicao_nome = True

while condicao_nome:  
    nome = input("Qual é o seu nome?\n")

    if validar_nome(nome):
        user_input = input(f"Essa informação está correta? Nome: {nome}\nsim ou não?\n").lower().strip()
        if confirmar(user_input):
            condicao_nome = False
        else:
            print("Vamos tentar novamente.")
    else:
        print("Digite apenas letras. Números ou caracteres especiais não são válidos.")

def validar_idade(data_nascimento):
    if re.fullmatch(r"^(?:0[1-9]|[12]\d|3[01])([\/.-])(?:0[1-9]|1[012])\1(?:19|20)\d\d$", data_nascimento):
        return True
    else:
        return False

condicao_data_nascimento = True

while condicao_data_nascimento:
    data_nascimento = input("Digite a sua data de nascimento, no formato DD/MM/AAAA.\n")

    if validar_idade(data_nascimento):
        user_input = input(f"Essa informção está correta? Data de nascimento: {data_nascimento}\nsim ou não?\n")
        if confirmar(user_input):
            condicao_data_nascimento = False
    else:
        print("Vamos tentar novamente. \nExemplo: 01/01/2000, 01.01.2000 ou 01-01-2000\n")

print("Perfeito! Vamos prosseguir com seu atendimento.\n")

opcao = input(...)
