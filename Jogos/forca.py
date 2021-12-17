import random
def jogar():
    print("---------------------------------")
    print("Bem vindo ao jogo da forca")
    print("---------------------------------")


    arquivo = open("frutas.txt", "r")
    frutas = []


    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)


    arquivo.close()

    numero = random.randrange(0, len(frutas))


    arquivo_times = open("times.txt", "r")
    times = []

    for linha in arquivo_times:
        linha = linha.strip()
        times.append(linha)

    arquivo_times.close()

    numero_times = random.randrange(0, len(times))

    print("#TEMAS DISPONIVEIS#")
    print("(1) FRUTAS  (2) TIMES")
    escolha = int(input("Digite sua escolha: "))

    if (escolha == 1):
        palavra_secreta = frutas[numero].upper()
        letras_acertadas = ["_" for letra in palavra_secreta]



    elif (escolha == 2):
        palavra_secreta = times[numero_times].upper()
        letras_acertadas = ["_" for letra in palavra_secreta]


    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite a letra: ")
        chute = chute.strip().upper()


        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()

    elif(enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

    print("O que você deseja?")
    print("(1) ADICIONAR PALAVRAS EM CATEGORIAS EXISTENTES")
    print("(2) ADICIONAR UMA CATEGOIRA (4 PALAVRAS)")
    print("(3) ENCERRAR")
    opcao_final = int(input("ESCOLHA: "))

    if(opcao_final == 1):

        categoria_add = int(input("Escolha a categoria para ser adicionada a palavra ----- (1) FRUTAS  (2) TIMES  "))

        if (categoria_add == 1):
            adicionar_fruta()

        elif(categoria_add == 2):
            adicionar_times()

    elif(opcao_final == 2):
        criar_tema()

    elif (opcao_final == 3):
        print("Fim de jogo")







def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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


def adicionar_fruta():

        fruta_adicionada = input("Qual fruta deseja adicionar: ")

        arquivo_addfrutas = open("frutas.txt", "a")

        arquivo_addfrutas.write('\n')
        arquivo_addfrutas.write(fruta_adicionada)

        print("Você adicionou: {}".format(fruta_adicionada))

        arquivo_addfrutas.close()

def adicionar_times():

        time_adicionado = input("Qual time deseja adicionar: ")

        arquivo_addtimes = open("times.txt", "a")

        arquivo_addtimes.write('\n')
        arquivo_addtimes.write(time_adicionado)

        print("Você adicionou: {}".format(time_adicionado))

        arquivo_addtimes.close()

def criar_tema():
    nome_categoria = input("Digite o nome da categoria: ")

    arquivo_novacategoria = open("{}.txt".format(nome_categoria), "w")

    aux = 0

    while (aux <= 3):
        palavras_novotema = input("Digite a palavra: ")
        arquivo_novacategoria.write(palavras_novotema)
        arquivo_novacategoria.write('\n')

        aux = aux + 1

    print("Parabéns, você criou a categora {} ".format(nome_categoria))


if (__name__ == "__main__"):
    jogar()
