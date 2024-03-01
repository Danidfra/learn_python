from random import randint;

maior = 0
menor = 0

tupla_nmr = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)


for p, i in enumerate(tupla_nmr):
    if i > maior:
        maior = i

    if p == 0:
        menor = i

    elif i < menor:
        menor = i 


print(f'Os valores sorteados foram: ', end='')

for i in tupla_nmr:
    print(f'{i} ', end='')

print('\nUniversal: ')
print(f'O maior valor sorteado foi {maior}.')
print(f'O menor valor sorteado foi {menor}.')

print('Recurso do python: ')
print(f'O maior valor sorteado foi {max(tupla_nmr)}.')
print(f'O menor valor sorteado foi {min(tupla_nmr)}.')
