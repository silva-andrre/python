from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
if tmaior == 0:
    print('Todas as pessoas são menores de idade.')
elif tmenor == 0:
    print('Todas as pessoas são maiores de idade.')
else:
    print('Ao todo tivemos {} pessoas maiores de idade.'.format(tmaior))
    print('E também tivemos {} pessoas menores de idade.'.format(tmenor)
    
