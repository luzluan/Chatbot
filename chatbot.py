def dados():
    nome = input("Olá, diga seu nome.\n")
    idade = int(input("Agora, a sua idade.\n"))
    print("Então, seu nome é", nome, "e sua idade é", idade) 

answer = input("\nCorreto?\n s ou n")
if answer == "s":
        print("Perfeito. Vamos prosseguir!")
elif answer == "n":
        return dados
else: print("Vamos tentar novamente.")