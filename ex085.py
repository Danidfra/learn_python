lista_nmr_par = list()
lista_nmr_impar = list()
lista_nmr = [lista_nmr_par, lista_nmr_impar]

qnt_nmr = int(input('Quantos números quer informar? '))

for i in range(0, qnt_nmr):
    nmr = int(input(f'Digite o {i + 1}º valor: '))

    if nmr % 2 == 0:
        lista_nmr[0].append(str(nmr))
    else:
        lista_nmr[1].append(str(nmr))
    
lista_str_par = ', '.join(lista_nmr[0])
lista_str_impar = ', '.join(lista_nmr[1])

print(f'Os valores pares digitados foram: {lista_str_par}.')
# for i in lista_nmr_par:
#     print(f'{i}')
# print(f'Os valores ímpares digitados foram: ', end='')
print(f'Os valores ímpares digitados foram: {lista_str_impar}.')

print(f'A lista completa é: {lista_nmr}')
