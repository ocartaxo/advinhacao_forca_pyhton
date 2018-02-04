
def jogar():
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

    palavra_secreta = "banana".upper()

    palavras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou  = False
    erros = 0

    print(palavras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    palavras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in palavras_acertadas
        print(palavras_acertadas)


    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()