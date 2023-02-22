import random

def jogar_forca():
    print("----------------------------------")
    print("   Bem vindo ao jogo de forca!")
    print("----------------------------------")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou = False
    enforcou = False
    erros = 0

    print("Palavra:\n", letras_acertadas,"\n")

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta: #Para cada letra na palavra secreta
                if(chute == letra):
                    letras_acertadas[index] = letra # Se acertar vou sobrescrever sobre a posição certa
                index += 1
        else:
            erros += 1
            print("Ops, não tem essa letra! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas #Não acertou enquanto _ estiver nas letras acertadas
        print(letras_acertadas)

    if (acertou):
        print("---------------------------------")
        print("Parabens, você acertou!!","\nA palavra sercreta era:", palavra_secreta)
    else:
        print("---------------------------------")
        print("Você perdeu!")
        print("\nA palavra sercreta era:", palavra_secreta)

    print("Jogo encerrado")
    print("---------------------------------")

if (__name__ == "__main__"):
    jogar_forca()