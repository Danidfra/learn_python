

def fatorial(n, show=False):
    """"
    -> Calcula o Fatorial de um número:
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    c = 1
    if show:
        frase = ''
        for i in range(n, 0, -1):
            c *= i
            if i != 1:
                frase = frase + str(i) + ' x '
            else:
                frase = frase + str(i) + ' = '

        print(frase, end='')
    else:
        for i in range(n, 0, -1):
            c *= i
    return c

nmr = int(input('Gostaria de calcular o fatorial de qual número? '))

mostrar = True if input('Gostaria de ver o calculo completo? S/N ') in 'sS' else False

resultado = fatorial(nmr, mostrar)

print(resultado)

# help(fatorial)