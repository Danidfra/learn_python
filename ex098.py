from time import sleep;

# Criando função
def linha():
    print('-+-'*20)

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for n in range(i, (f + 1), p):
        print(f'{n} ', end='')
    print('FIM!')
    linha()

# PROGRAMA PRINCIPAL
linha()
contador(1, 10, 1)
contador(10, 1, -1)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)