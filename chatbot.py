import re

print("Olá!\nSou *****, e vou te auxiliar na triagem do seu atendimento. Para iniciarmos:")

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
        print("Vamos tentar novamente. \nExemplo: 01/01/2000\n")

print("teste")


# if re.fullmatch(r"^[a-zA-Z]+$", nome):
#     print("Tente inserir seu nome novamente.")
#     nome = input("Qual é o seu nome?\n")
# idade = input("Agora, qual é a sua idade?\n")
# verificar = print("Seu nome é", nome, "e a sua idade é", idade)


# def dados():

#     nome= input("Olá, diga seu nome.\n")
#     print(validar_letras(nome))
#     idade = int(input("Agora, a sua idade.\n"))
#     print("Então, seu nome é", nome, "e sua idade é", idade)

# def validar_letras(entrada):
#     if re.fullmatch(r"^[a-zA-Z]+$", entrada):
#         return True
#     return False



# if validar_letras(entrada):
#     print("Entrada válida!")
# else:
#     print("Entrada inválida. Apenas letras são permitidas.")



# answer = input("\nCorreto?\n s ou n\n")
# if answer == "s":   
#     print("Perfeito. Vamos prosseguir!")
# elif answer == "n":
#     dados()
# else:
#     print("Tente responder com S ou N.")

# #verificação se tem registro dos dados no banco (função)

# print("Vimos que você já está registrado. No que podemos ajudar?")
