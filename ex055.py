
# conjunto = []


# for i in range(0, 5):
#     peso = float(input(f'Peso da {i + 1}ª pessoa: '))
#     conjunto.append(peso)

# for i in range(0, len(conjunto)):
#     for c in range(0, len(conjunto)):
#         if conjunto[i] < conjunto[c]:
#             continue
#         else:
#             print(conjunto[i],conjunto[c])
#             aux_1 = conjunto[i]
#             conjunto[i] = conjunto[c]
#             conjunto[c] = aux_1
#             print(conjunto[i],conjunto[c])
        
# print(f'O maior peso foi {conjunto[0]}.')

# conjunto.reverse()

# print(f'O menor peso foi {conjunto[0]}.')

maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input(f'Peso da {i + 1}ª pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso foi {maior}.')
print(f'O menor peso foi {menor}.')