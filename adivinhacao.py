print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite um número: ")

print("Você digitou: ", chute_str)

chute = int(chute_str)

if(chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")
