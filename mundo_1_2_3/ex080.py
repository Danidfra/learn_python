conjunto_nmr = list()

qnt_nmr = int(input('Quantos números quer adicionar a lista? '))

for i in range(0, qnt_nmr):
    nmr = int(input('Digite um valor: '))

    if i == 0 or nmr > conjunto_nmr[len(conjunto_nmr) - 1]:
        conjunto_nmr.append(nmr)
        print('Valor adicionado ao final da lista... ')

    else:
        pos = 0

        while pos < len(conjunto_nmr):
            if nmr <= conjunto_nmr[pos]:
                conjunto_nmr.insert(pos, nmr)
                print(f'Valor adicionado a posição {pos} da lista... ')
                break
            pos += 1

print(conjunto_nmr)