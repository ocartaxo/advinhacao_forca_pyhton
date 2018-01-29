import random

print("*****************************************")
print("*** Bem vindo ao jogo de Adivinhação! ***")
print("*****************************************")

numero_secreto = round(random.randrange(1, 101))
tota_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil  (2) Médio  (3) Difícil")
dificuldade_valida = False

while(not dificuldade_valida):
    nivel = int(input("Defina a dificuldade: "))

    if (nivel == 1):
        tota_de_tentativas = 20
        dificuldade_valida = True
    elif (nivel == 2):
        tota_de_tentativas = 10
        dificuldade_valida = True
    elif (nivel == 3):
        tota_de_tentativas = 5
        dificuldade_valida = True
    else:
        print("Por favor, insira um nível de dificuldade válido.")

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
        print("Parabéns, você acertou! Sua pontuação foi {}".format(pontos))
        acertou = True
        break
    else:
        if (eh_maior):
            print("O seu chute foi MAIOR que o número secreto.")
        elif (eh_menor):
            print("O seu chute foi MENOR que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo!")