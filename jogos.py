import adivinhacao
import forca
import time

print("*********************")
print("*** Menu de jogos ***")
print("*********************")

print("\nJogos disponíveis.:")
print("(1) Adivinhação  (2) Forca")

escolha = int(input("Escolha o seu jogo: "))

if(escolha == 1):
    print("Jogo da Adivinhação escolhido.")
    print("Carregando...")
    time.sleep(2)
    adivinhacao.jogar()
elif(escolha == 2):
    print("Jogo da Forca escolhido")
    print("Carregando...")
    time.sleep(2)
    forca.jogar()