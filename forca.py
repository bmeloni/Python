def jogar_forca():
    print("----------------------------------")
    print("   Bem vindo ao jogo de forca!")
    print("----------------------------------")

    palavra_secreta = "banana"

    acertou = False
    enforcou = False

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        index = 0 #Index = posição
        for letra in palavra_secreta: #Para cada letra na palavra secreta
            if(chute.upper() == letra.upper()):
                print("Letra {} encontrada na posiçao {}".format(letra,index))
            index = index + 1

    print("Jogo encerrado!")
    print("---------------------------------")

if (__name__ == "__main__"):
    jogar_forca()