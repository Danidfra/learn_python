from time import sleep;

i = int(input('Qual o número inicial? '))
f = int(input('Qual o número final? '))
tipo = input('Você quer que eu faça a contagem de números pares ou impares? pares/impares ').lower().strip()

alterar_velocidade = input('Você quer mudar a velocidade que será contado? S/N ').lower().strip()

if alterar_velocidade == 's':
    velocidade_contagem = float(input('Quanto tempo devo demorar a cada contagem (quantos segundos)? '))
else:
    velocidade_contagem = 0

if tipo == 'pares':
    for c in range(i, f+1):
        if c%2 == 0:
            sleep(velocidade_contagem)
            print(c)

elif tipo == 'impares':
    for c in range(i, f+1):
        if c%2 != 0:
            sleep(velocidade_contagem)
            print(c)



print('Fim')