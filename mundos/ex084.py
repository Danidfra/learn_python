lista_pessoas = list()
qnt_pessoas = 0
pesos = []
p_maior_peso = list()
p_menor_peso = list()

while True:
    nome = input('Digite seu nome: ').strip().title()
    peso = float(input('Digite seu peso(kg): '))


    lista_pessoas.append([nome, peso])
    pesos.append(peso)
    qnt_pessoas += 1

    continuar = input('Quer continuar? S/N ')

    while continuar not in 'nNsS':
        print(('Opção inválida! '))
        continuar = input('Quer continuar? S/N ')

    if continuar in 'nN':
        break

nmr_maior_peso = 0

for i in pesos:
    if i > nmr_maior_peso:
        nmr_maior_peso = i


nmr_menor_peso = min(pesos)

for c,i in enumerate(pesos):
    if i == nmr_maior_peso:
        p_maior_peso.append(lista_pessoas[c])
    elif i == nmr_menor_peso:
        p_menor_peso.append(lista_pessoas[c])

print('-=-'*40)

print(f'Foram cadastradas {qnt_pessoas} pessoas ao todo. ')

print(f'O maior peso foi de {p_maior_peso[0][1]} Kg. Peso de ', end='')
for c, i in enumerate(p_maior_peso):
    if c == (len(p_maior_peso) - 1):
        print(f'{i[0]}.')
    else:
        print(f'{i[0]}, ', end='')

print(f'O menor peso foi de {p_menor_peso[0][1]} Kg. Peso de ', end='')
for c, i in enumerate(p_menor_peso):
    if c == (len(p_menor_peso) - 1):
        print(f'{i[0]}.')
    else:
        print(f'{i[0]}, ', end='')



# print(lista_pessoas)
# print(p_maior_peso) 
# print(p_menor_peso)
