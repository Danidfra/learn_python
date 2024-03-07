lista_nmr_par = list()
lista_nmr_impar = list()
lista_nmr = [lista_nmr_par, lista_nmr_impar]

qnt_nmr = int(input('Quantos números quer informar? '))

for i in range(0, qnt_nmr):
    nmr = int(input(f'Digite o {i + 1}º valor: '))

    if nmr % 2 == 0:
        lista_nmr[0].append(nmr)
    else:
        lista_nmr[1].append(nmr)

lista_nmr[0].sort()
lista_nmr[1].sort()

print('Os valores pares digitados foram: ', end='')
for c, i in enumerate(lista_nmr_par):
    if c == (len(lista_nmr_par) - 1 ):
        print(f'{i}.')
    else:
        print(f'{i}, ')
print(f'Os valores ímpares digitados foram: ', end='')
for d, j in enumerate(lista_nmr_impar):
    if d == (len(lista_nmr_impar) - 1 ):
        print(f'{j}.')
    else:
        print(f'{j}, ')

print(f'A lista completa é: {lista_nmr}')