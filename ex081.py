conj_nmr = list()

while True:
    nmr = int(input('Digite um valor: '))

    conj_nmr.append(nmr)

    continuar = input('Quer continuar? S/N ')

    while continuar not in 'SsNn':
        print('Opção invalida! ')
        continuar = input('Quer continuar? S/N ')

    if continuar in 'Nn':
        break

qnt_cinco = conj_nmr.count(5)
lista_pos_cinco = list()

for p, i in enumerate(conj_nmr):
    if i == 5:
        lista_pos_cinco.append(p)
        # lista_pos_cinco.append(str(p))

print(lista_pos_cinco)
pos_cinco = ''
for i in lista_pos_cinco:
    pos_cinco += str(i) + '... '

# pos_cinco =  str("...".join(lista_pos_cinco))

conj_nmr.sort()
conj_nmr.reverse()

print(len(conj_nmr))
print(conj_nmr)
if 5 in conj_nmr:
    print(f'O valor 5 aparece na lista {qnt_cinco} vezes, nas posições {pos_cinco}')