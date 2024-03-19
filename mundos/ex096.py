# Criando função que retorna o resultado
def calcArea(x, y):
    r = x * y
    return r 

# PROGRAMA PRINCIPAL
print('-+-'*10)
print(f'    Controle de Terrenos    ')
print('-+-'*10)

## Declarando variaveis
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

## Armazenando retorno da função
resultado = calcArea(largura, comprimento)

print(f'A área de um terreno com {largura}(l) x {comprimento}(c) é de {resultado:.2f} m².')