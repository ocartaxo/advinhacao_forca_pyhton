import random

print("***************************************")
print("** Bem vindo ao jogo de Adivinhação! **")
print("***************************************")

numero_secreto = round(random.randrange(1, 101) * 100) # 1 >= numero_secreto <= 100
tota_de_tentativas = 3

acertou = False

for rodada in range(1, tota_de_tentativas+1):

    print("Tentaiva {} de {}".format(rodada, tota_de_tentativas))
    chute_str = input("Chute um número inteiro entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você digitou um número inválido.")
        continue

    acertou = chute == numero_secreto
    eh_maior = chute > numero_secreto
    eh_menor = chute < numero_secreto

    if (acertou):
        print("Parabéns! Você acertou!")
        acertou = True
        break
    else:
        if (eh_maior):
            print("O seu chute foi MAIOR que o número secreto.")
        elif (eh_menor):
            print("O seu chute foi MENOR que o número secreto.")

if(not acertou):
    print("Você perdeu, que pena. O número secreto era {}.".format(numero_secreto))
else:
    print("Você venceu, muito bem!!")

print("Fim de jogo!")