import random
def jogar():


    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação")
    print("---------------------------------")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print ("NÍVEIS DE DIFICULDADE")
    print (" (1) Fácil  (2) Médio  (3) Díficil")
    nivel = int(input("Escolha o nível : "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    elif(nivel ==- 3):
        tentativas == 5


    for rodada in range(1, tentativas + 1):

        print("Tentativa {} de {}".format(rodada, tentativas))

        chute_str = input("Digite um número de 1 à 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("Seu número é inválido, digite novamente!")
            continue



        acertou = numero_secreto == chute
        errou_maior = numero_secreto < chute
        errou_menor = numero_secreto > chute

        if (acertou):
            print("ACERTOU")
            print("Sua pontuação foi de {}".format(pontos))
            print("-------------------------------------------------")
            break
        else:
            if (errou_maior):
                print("ERROU! Seu chute está maior que o número secreto")
                print("-------------------------------------------------")
            elif (errou_menor):
                print("ERROU! Seu chute está menor que o número secreto")
                print("-------------------------------------------------")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("O número era {}".format(numero_secreto))
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()