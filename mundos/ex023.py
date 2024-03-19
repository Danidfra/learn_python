nmr = input('Por favor, me forneça um número de 0 a 9999... ')


if len(nmr) == 1:
    u = nmr[0]

    print(f'unidade: {u}')

elif len(nmr) == 2:
    u = nmr[1]
    d = nmr[0]

    print(f'unidade: {u}')
    print(f'dezena: {d}')

elif len(nmr) == 3:
    u = nmr[2]
    d = nmr[1]
    c = nmr[0]

    print(f'unidade: {u}')
    print(f'dezena: {d}')
    print(f'centena: {c}')

elif len(nmr) == 4:
    u = nmr[3]
    d = nmr[2]
    c = nmr[1]
    m = nmr[0]

    print(f'unidade: {u}')
    print(f'dezena: {d}')
    print(f'centena: {c}')
    print(f'milhar: {m}')