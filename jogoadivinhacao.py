import random;
def jogar_adivinhção():

    print('*********************************')
    print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
    print('*********************************')

    #definindo o  numero secreto
    numeroSecreto = random.randrange(1,101)
    #print(numeroSecreto)


    #Definindo o numero de tentativas
    numerotentativas = 0
    rodada=1
    pontos = 1000

    print(" Qual o nível de dificuldade?")
    print("(1)-Facíl,(2)-médio,(3)-difícil")

    nivel = int(input("Defina o nível:"))

    #vamos mudar o numero de tentativas conforme a dificuldade
    if(nivel == 1):
        numerotentativas=18
    elif(nivel==2):
        numerotentativas=8
    else:
        numerotentativas=5

    while(rodada<= numerotentativas):
        print('tentativa',rodada, 'de',numerotentativas)


    #Recebendo o chute do jogador
        chuteString = input('Digite um número: ')


        chute = int (chuteString)

    #Declarando as condições
        if (numeroSecreto == chute):
            print('Você acertou!e sua pontuação foi:', pontos)
            break
        elif(chute>numeroSecreto):
            print('Voce errou!! O número secreto é numero menor')
        else:
            print('Você errou!! O numero secreto é um número maior')
        pontos_perdidos = abs(numeroSecreto - chute);
        pontos = pontos - pontos_perdidos

        #numerotentativas = numerotentativas - 1
        rodada = rodada + 1






