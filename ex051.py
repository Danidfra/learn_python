

possivel_palindromo= input('Digite aqui a sua palavra ou frase: ').lower().strip()
is_palindromo = 'é um palindromo'


carac_formatado = possivel_palindromo.split()
carac_formatado = ''.join(carac_formatado)
trans_lista = list(carac_formatado)
print(trans_lista)
# trans_lista_reverse = inverte(trans_lista)

for i in range(0, len(trans_lista)):
    print(i)
    if trans_lista[i] != trans_lista[(len(trans_lista) - 1) - i]:
        is_palindromo = 'não é um palindromo'


print(f'O item {is_palindromo}.')