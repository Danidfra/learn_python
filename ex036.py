from time import sleep;
from math import ceil;

valor_casa = float(input('Qual o valor do imovel desejado? '))
salario_comprador = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos planeja terminar de pagar? '))


valor_mensal = valor_casa / (anos * 12) ## Calcula o valor mensal a ser pago.

porcentagem_salario = salario_comprador * 0.30 ## Calcula o valor de 30% do salario.

anos_ajustado = ceil((valor_casa / porcentagem_salario) / 12) ## Calcula a quantidade de anos que seriam necessarios para pagar a casa.

valor_mensal_ajustado = valor_casa / (anos_ajustado * 12)

if valor_mensal < porcentagem_salario:
    print('PROCESSANDO...')
    sleep(3)
    print(f'Seu empréstimo foi aprovado! Parabéns... \nO valor mensal a ser pago será de R${valor_mensal:.2f} por mes. ')
elif valor_mensal > porcentagem_salario:
    print('PROCESSANDO...')
    sleep(3)
    print('O empréstimo foi negado! ')
    print(f'Para o valor deste empréstimo ser aprovado \nvocê teria de aumentar o tempo de pagamento para {anos_ajustado} anos\nlevando em conta seu salario atual de R${salario_comprador:.2f}\npagando o valor de R${valor_mensal_ajustado:.2f} por mes. ')


