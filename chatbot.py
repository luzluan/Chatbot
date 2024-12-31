import re

print("Olá!\nSou *****, e vou te auxiliar na triagem do seu atendimento. Para iniciarmos:")

def validar_nome(nome):
    if re.fullmatch(r"^[a-zA-Z]+$", nome):
        return True
    else:
        return False

condicao_nome = True

while condicao_nome:
    
    nome = input("Qual é o seu nome?\n")

    if validar_nome(nome):
        condicao_nome = False
    else:
        print("Vamos tentar novamente.")

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
