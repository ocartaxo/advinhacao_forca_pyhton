print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

numero_secreto = 42

chute_str = input("Digite um número: ")

print("Você digitou: ", chute_str)

chute = int(chute_str)

acertou  = chute == numero_secreto
eh_maior = chute > numero_secreto
eh_meor  = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(eh_maior):
        print("Você errou! O seu chute é maior que o número secreto.")
    elif(eh_menor):
        print("Você errou! O seu chute é menor que o número secreto.")

print("Fim de jogo!")