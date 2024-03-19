nome = input('Me informe seu nome completo por favor: ')


nome_lower = nome.lower()


re = nome_lower.split()


def testa_silva():
    return 'silva' in re


if testa_silva():
    p = re.index('silva')
    print(f'O nome {nome} contém a palavra Silva! E a palavra Silva esta no {p + 1}˚ lugar')

else:
    print(f'O nome {nome} não contém a palavra Silva! ')

