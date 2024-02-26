print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 17

chuteString = input('Digite um número')
#chuteString = input('Digite um número')#

print('Você digitou o número', chuteString)

chute = int(chuteString)

if numeroSecreto == chute:
    print('Você acertou!')
elif(chute>numeroSecreto):
   print('voce errou!! o numero secreto é um numero menor')
else:
    print('Você errou!! o numero secreto e um numero maior')

