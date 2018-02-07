import random

import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

    print("Fim do jogo")


def imprime_mensagem_vencedor():
    print("Você ganhou!")

def imprime_mensagem_perdedor():
    print("Você perdeu!")

def imprime_mensagem_abertura():
    # Mensagem de início
    print("***********************************")
    print("*** Bem vindo ao jogo da Forca! ***")
    print("***********************************")

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    return chute

def carrega_palavra_secreta():
    frutas = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            frutas.append(linha)

    numero = random.randrange(0, len(frutas))

    palavra_secreta = frutas[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Compreensão de lista (List Comprehension)


if(__name__ == "__main__"):
    jogar()