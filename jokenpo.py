from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[7mJO\033[m')
sleep(1)
print('\033[7mKEN\033[m')
sleep(1)
print('\033[7mPO!!!\033[m')
print(' ')
print('\033[35m-=\033[m' * 12)
print('Computador jogou \033[36m{}\033[m'.format(itens[pc]))
print('Jogador jogou \033[36m{}\033[m'.format(itens[jogador]))
print('\033[35m-=\033[m' * 12)
print(' ')
if pc == 0: #PC PEDRA
    if jogador == 0:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    else:
        print('Jogada INVÁLIDA!')
elif pc == 1: #PC PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU!\033[m')
    else:
        print('Jogada INVÁLIDA!')
elif pc == 2: #PC TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE!\033[m')
    else:
        print('Jogada INVÁLIDA!')
