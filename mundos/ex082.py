lista_nmr = list()
lista_pares = list()
lista_impares = list()


while True:
    nmr = int(input('Digite um número: '))

    lista_nmr.append(nmr)
    if nmr%2 ==0 and nmr not in lista_pares:
        lista_pares.append(nmr)
    elif nmr % 2 != 0 and nmr not in lista_pares:
        lista_impares.append(nmr)

    continuar = input('Quer continuar? S/N ')
    while continuar not in 'SsNn':
        print('Opção invalida! ')
        continuar = input('Quer continuar? S/N ')

    if continuar in 'NnnãoNãonaoNao':
        break


print(f'A lista completa é {lista_nmr}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')