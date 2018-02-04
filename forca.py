def jogar():
    #Mensagem de início
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta] # Compreensão de lista (List Comprehension)

    enforcou = False
    acertou  = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou. Agora voê tem {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabéns, você ganhou!!")
    else:
        print("Parabéns, você perdeu!!")

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()