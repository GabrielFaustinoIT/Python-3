import forca
import adivinhacao

print("---------------------------------------")
print("          ESCOLHA SEU JOGO             ")
print("---------------------------------------")

print("#Jogos disponíveis#")
print("(1) Adivinhção  (2) Forca")
jogo = int(input("Qual vai jogar agora? "))

if(jogo == 1 ):
    print("Jogando adivinhação...")
    adivinhacao.jogar()
elif(jogo == 2 ):
    print("Jogando forca...")
    forca.jogar()
else:
    print("Jogo indisponível")
