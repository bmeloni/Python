import random

print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = round(random.random() * 100) #0.0 e 1.0
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 0 e 100: ")
    print("\nVocê digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 0 or chute > 100):
        print("Número digitado inválido, vcocê deve digitar um número entre 0 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("\nParabéns, você acertou o número!")
        break
    else:
        if (maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")

print("Fim de jogo")