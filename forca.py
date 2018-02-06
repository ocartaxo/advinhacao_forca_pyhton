import random

def jogar():
    
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = incializa_letras_acertadas(palavra_secreta)

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



def imprime_mensagem_abertura():
    # Mensagem de início
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

def carrega_palavra_secreta():
    frutas = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            frutas.append(linha)

    numero = random.randrange(0, len(frutas))

    palavra_secreta = frutas[numero].upper()
    return palavra_secreta


def incializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Compreensão de lista (List Comprehension)


if(__name__ == "__main__"):
    jogar()