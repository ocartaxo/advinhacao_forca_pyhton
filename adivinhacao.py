print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

numero_secreto = 42

tota_de_tentativas = 3
rodada = 1
ganhou = False

while (rodada <= tota_de_tentativas and not(ganhou) ):

    print("Tentaiva {} de {}".format(rodada, tota_de_tentativas))
    chute_str = input("Digite um número: ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    eh_maior = chute > numero_secreto
    eh_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        gahou = True
    else:
        if (eh_maior):
            print("Você errou! O seu chute é maior que o número secreto.")
        elif (eh_menor):
            print("Você errou! O seu chute é menor que o número secreto.")

    rodada += 1

print("Fim de jogo!")