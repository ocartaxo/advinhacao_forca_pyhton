import adivinhacao
import forca
import time

print("**************************")
print("*** Escolha o seu jogo ***")
print("**************************")

print("(1) Adivinhação  (2) Forca")

escolha = int(input("Escolha o seu jogo: "))

if(escolha == 1):
    print("Jogo da Adivinhação escolhido.")
    print("Carregando...")
    time.sleep(3)
    adivinhacao.jogar()
elif(escolha == 2):
    print("Jogo da Forca escolhido")
    print("Carregando...")
    time.sleep(3)
    forca.jogar()