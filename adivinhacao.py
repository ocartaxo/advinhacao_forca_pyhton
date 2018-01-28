print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

numero_secreto = 42

tota_de_tentativas = 3


for rodada in range(1, tota_de_tentativas+1):

    print("Tentaiva {} de {}".format(rodada, tota_de_tentativas))
    chute_str = input("Chute um número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    eh_maior = chute > numero_secreto
    eh_menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if (eh_maior):
            print("O seu chute foi MAIOR que o número secreto.")
        elif (eh_menor):
            print("O seu chute foi MENOR que o número secreto.")

print("Fim de jogo!")