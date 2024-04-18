import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto
numeroSecreto = random.randrange(1,101)
#print(numeroSecreto)

#Definindo o número de tentativas e rodada
numeroTentativas = 10
rodada = 1

print('qual o seu nivel de dificuldade?')
print('(1)-facil, (2)medio,(3)- dificil, (4)- hardone')

nivel= int(input("define um nivel"))
#vamos mudar o numero de tentativas conforme a dificuldade

if(nivel == 1):
    numerotentativas = 15

    elif(nivel == 2):
        numerotentativas = 8
elif(nivel == 3):
    numeroTentativas = 5

else:
    numeroTentativas = 2
    
while(rodada <= numeroTentativas):
    print('Tentativa',rodada, 'de' , numeroTentativas)

#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')

    #numeroTentativas = numeroTentativas - 1
    rodada = rodada + 1



#Aula Elif 26.02.24

