

def testa_palindromo():
    possivel_palindromo= input('Digite aqui a sua palavra ou frase: ').lower().upper()
    is_palindromo = 'é um palíndromo'

    tipo = 'frase' if ' ' in possivel_palindromo else 'palavra'

    carac_formatado = possivel_palindromo.split()
    carac_formatado = ''.join(carac_formatado)
    trans_lista = list(carac_formatado)
    formando_reverse = ''

    for i in range(0, len(trans_lista)):
        formando_reverse += trans_lista[(len(trans_lista)- 1) - i]
        if trans_lista[i] != trans_lista[(len(trans_lista) - 1) - i]:
            is_palindromo = 'não é um palíndromo'


    print(f'O inverso de {carac_formatado} é {formando_reverse}.\nA {tipo} {is_palindromo}.')
    
    pergunta_continuar = input('Gostaria de testar outra palavra ou frase? S/N').lower().strip()

    if pergunta_continuar == 's':
        testa_palindromo()
    else:
        print('Tchau tchau, caso queira testar outros valores sabe onde me encontrar! ')





testa_palindromo()

