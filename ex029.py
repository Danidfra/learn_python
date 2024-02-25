velocidade_carro = float(input('Qual é a velocidade atual do carro? '))


if velocidade_carro <= 80:
    print('Você esta dentro da velocidade permitida, obrigado por respeitar as normas de transito! ')
    print('Tenha um bom dia! Dirija com segurança! ')
else:
    valor_multa = (velocidade_carro - 80) * 7
    print(f'Multado! Você excedeu o limite permitido que é de 80 km/h \n Você deve pagar uma multa de R${valor_multa:.2f}! ')
    print('Tenha um bom dia! Dirija com segurança! ')