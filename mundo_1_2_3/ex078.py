conjunto_valores = list()
posicoes_maior = list()
posicoes_menor = list()
p_maior_formatado = ''
p_menor_formatado = ''

qnts_valores_adicionar = int(input('Você quer adicionar quantos valores a sequencia? '))

for i in range(0 , qnts_valores_adicionar):
    conjunto_valores.append(int(input(f'Digite um valor para a posição {i}: ')))

maior_valor = max(conjunto_valores)
menor_valor = min(conjunto_valores)

qnt_maior = conjunto_valores.count(maior_valor)
qnt_menor = conjunto_valores.count(menor_valor)


for p, c in enumerate(conjunto_valores):
    if c == maior_valor:
        posicoes_maior.append(p)

for p, c in enumerate(conjunto_valores):
    if c == menor_valor:
        posicoes_menor.append(p)

for i in range(0, len(posicoes_maior)):
    p_maior_formatado += str(posicoes_maior[i]) + '... '

for i in range(0, len(posicoes_menor)):
    p_menor_formatado += str(posicoes_menor[i]) + '... '


print(f'Você digitou os valores: {conjunto_valores}')

if qnt_maior >1:
    print(f'O maior valor digitado foi {maior_valor}, nas posições {p_maior_formatado}')
else:
    print(f'O maior valor digitado foi {maior_valor}, na posição {p_maior_formatado}')

if qnt_menor >1:
    print(f'O menor valor digitado foi {menor_valor}, nas posições {p_menor_formatado}')
else:
    print(f'O menor valor digitado foi {menor_valor}, na posição {p_menor_formatado}')
