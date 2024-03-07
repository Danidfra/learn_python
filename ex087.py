matriz = [[], [], []]

for c, i in enumerate(matriz):
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{c}, {j}]: '))
        matriz[c].append(valor)

print('=-='*30)

soma_pares = 0
soma_coluna_3 = 0

for i in matriz:
    for j in i:
        # Somando pares
        if j% 2 ==0:
            soma_pares += j
        # Imprimindo a matriz
        print(f'[{j:5}]', end='')
    print()

print('=-='*30)
print(f'A soma dos valores pares é {soma_pares}.')

for i in matriz:
    soma_coluna_3 += i[2]

print(f'A soma dos valores da terceira coluna é {soma_coluna_3}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
