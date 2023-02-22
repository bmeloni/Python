import random

def imprime_mensagem_abertura():
    print("----------------------------------")
    print("   Bem vindo ao jogo de forca")
    print("----------------------------------")

def leitura_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_palavras_acertadas(palavra):
    return ["_" for letra in palavra]

def le_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def imprime_mensagem_ganhador(palavra_secreta):
    print("\n-----------------------------------")
    print("Parabens, você acertou!!", "\nA palavra sercreta era: {}".format(palavra_secreta))

def imprime_mensagem_perdedor(palavra_secreta):
    print("\n-----------------------------------")
    print("Você perdeu!")
    print("\nA palavra sercreta era: {}".format(palavra_secreta))

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar_forca():
    imprime_mensagem_abertura()
    palavra_secreta = leitura_palavra_secreta()

    letras_acertadas = inicializa_palavras_acertadas(palavra_secreta)
    print("A palavra é uma fruta:\n", letras_acertadas, "\n")

    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):
        
        chute = le_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            print("Ops, não tem essa letra!\nFaltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas #Não acertou enquanto _ estiver nas letras acertadas
        
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("-----------------------------------")

if (__name__ == "__main__"):
    jogar_forca()