def leiaInt(f):
    nmr = input(f)
    while not nmr.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        nmr = input(f)
    if nmr.isnumeric():
        return int(nmr)


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')