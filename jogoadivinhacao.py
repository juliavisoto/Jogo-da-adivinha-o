import random;

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número secreto50
numeroSecreto = random.randrange(1,101)

#print(numeroSecreto)

#Definindo o número de tentativas e rodada
numeroTentativas = 0
rodada = 1
pontos= 1000


print ("Qual o nível de dificuldade?")
print ("(1)-Fácil, (2)-Médio, (3)-Difícil")

nível = int (input('Defina o nível:'))

#Vamos mudar o número de tentativas conforme a difilculdade
if(nível == 1):
    numeroTentativas = 12
elif(nível == 2):
    numeroTentativas = 8
else:
    numeroTentativas = 5

while(rodada <= numeroTentativas):
    print('Tentativa',rodada, 'de' , numeroTentativas)

#Recebendo o chute do jogador
    chuteString = input('Digite um número entre 1 e 100: ')
    chute = int(chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!E sua pontuaçao foi:' ,pontos)
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
    pontos_perdidos = abs(numeroSecreto-chute)
    pontos = pontos - pontos_perdidos

    #numeroTentativas = numeroTentativas - 1
    rodada = rodada + 1



#Aula Elif 26.02.24

