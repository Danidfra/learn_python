def aumentar(n, p):
    return n * (1 + (p/100))
def diminuir(n, p):
    return n * (1 - (p / 100))
def dobro(n):
    return n * 2
def metade(n):
    return n/2


def formata(p):

    price_string = str(f'{p:,.2f}')
    price_cortado = list(price_string)

    for c, i in enumerate(price_cortado):
        if i == ',':
            price_cortado[c] = '.'
        elif i == ',':
            price_cortado[c] = ','

    price_formatado = ''.join(price_cortado)

    return 'R$'+ price_formatado


def resumo(p=0, a=0, r=0):
    print('-'*30)
    print(f'{'RESUMO DO VALOR'.center(30)}')
    print('-'*30)

    print(f'{'Preço analisado:':20} {formata(p)}')
    print(f'{'Dobro do preço:':20} {formata(dobro(p))}')
    print(f'{f'{a:.0f}% de aumento:':20} {formata(aumentar(p, a))}')
    print(f'{f'{r:.0f}% de redução:':20} {formata(diminuir(p, r))}')
