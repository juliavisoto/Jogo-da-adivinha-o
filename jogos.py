import forca
import jogoadivinhacao

print('*********************************')
print('********ESCOLHA O SEU JOGO!******')
print('*********************************')

print("(1) forca (2) adivinhação")

jogo = input(input("qual o jogo?"))

if(jogo == 1):
    print('jogando jogo da Forca')
    forca.jogar_forca()
else:
    print('jogando jogo da Adivinhação')
    jogoadivinhacao.jogar_adivinhção()