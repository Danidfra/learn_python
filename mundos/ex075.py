

nmr_1 = int(input('Digite um número: '))
nmr_2 = int(input('Digite um número: '))
nmr_3 = int(input('Digite um número: '))
nmr_4 = int(input('Digite um número: '))

tupla_nmrs = nmr_1, nmr_2, nmr_3, nmr_4

print(f'Você digitou os valores {tupla_nmrs}')
# if 9 in tupla_nmrs:
print(f'O valor 9 apareceu {tupla_nmrs.count(9)} vezes.')
if 3 in tupla_nmrs:
    print(f'O valor 3 apareceu na {tupla_nmrs.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
qnt_nmrs_pares = 0

for i in tupla_nmrs:
    if i % 2 == 0:
        qnt_nmrs_pares += 1

print(f'Foram digitados {qnt_nmrs_pares} número(s) par(es).')
