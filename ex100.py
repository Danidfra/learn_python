from random import randint;

def sorteia(x):
    """
    -> Sorteia uma certa quantidade de números e retorna uma lista com os números:
    :param x: Quantidade de números a serem sorteados
    :return: Retorna a lista_nmrs que foi criada na função
    """
    print(f'Sorteando {x} valores para a lista: ', end='')
    lista_nmrs = []
    for i in range(0, x):
        nmr = randint(1, 100)
        print(f'{nmr} ', end='')
        lista_nmrs.append(nmr)
    print('Pronto!')
    return lista_nmrs

def somaPar(num):
    soma_pares = 0
    for i in num:
        if i % 2 == 0:
            soma_pares += i
    return soma_pares

numeros = sorteia(int(input('Quantos números gostaria de sortear? ')))

s_par = somaPar(numeros)

print(f'Somando os valores pares da lista {numeros}, temos o resultado {s_par}.')   

# help(sorteia)