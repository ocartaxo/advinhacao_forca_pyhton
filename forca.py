
def jogar():
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

    palavra_secreta = "banana"

    palavras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou  = False

    print(palavras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Chute uma letra: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                palavras_acertadas[index] = letra
            index = index + 1

        print(palavras_acertadas)


    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()