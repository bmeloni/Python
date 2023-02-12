import adivinhacao
import forca

def escolhe_jogo():

    print("----------------------------------------------")
    print("Bem vindo, escolha qual jogo você deseja jogar")
    print("----------------------------------------------")

    print("1 - Jogo de Adivinhação\n2 - Jogo da Forca")

    print("----------------------------------------------")
    jogo = int(input("Digite o número do jogo escolhido: "))

    if (jogo == 1):
        print("Você escolheu o jogo de adivinhação\n")
        adivinhacao.jogar_adivinhacao()

    elif (jogo == 2):
        print("Você escolheu o jogo da forca\n")
        forca.jogar_forca()

if (__name__ == "__main__"):
    escolhe_jogo()