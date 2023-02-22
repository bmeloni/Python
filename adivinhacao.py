import random
def jogar_adivinhacao():
    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")

    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade do jogo:")
    print("1 - Fácil\n2 - Médio\n3 - Difícil")
    print("---------------------------------")

    nivel = int(input("Escolha o nível de dificuldade que você deseja jogar: "))
    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 0 e 100: ")
        print("\nVocê digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 0 or chute > 100):
            print("Número digitado inválido, você deve digitar um número entre 0 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("---------------------------------")
            print("Parabéns, você acertou o número!")
            print("Total de {} pontos: ".format(pontos))
            break

        else:
            if (maior):
                print("O seu chute foi maior que o número secreto")
            elif (menor):
                print("O seu chute foi menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("O número secreto era: {}".format(numero_secreto))
    print("-------------------------------------------")

if (__name__ == "__main__"):
    jogar_adivinhacao()