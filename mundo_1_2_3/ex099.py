
def maior(l_nums):
    maior = 0
    for i in l_nums:
        if i > maior:
            maior = i

    return maior


lista_numeros = []
qnt_nmr = int(input('Quantos números gostaria de adicionar? '))

for i in range(0, qnt_nmr):
    lista_numeros.append(int(input(f'Qual número deseja adicionar na {i + 1}ª posição? ')))

maior_nmr = maior(lista_numeros)
print('-+-'*20)
print(f'Foram informados {len(lista_numeros)} números ao todo.')
print(f'O maior número informado foi {maior_nmr}. ')