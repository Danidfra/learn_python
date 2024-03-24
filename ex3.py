from func.title import Tabela;
from func.calculator import calculadora


lst_op = ['Soma', 'Subtração', 'Multiplicação', 'Divisão' ,'Sair']

tab_calc = Tabela(50, lst_op)

while True:
    tab_calc.montar('Qual operação você gostaria de fazer? ',cab=True)

    choice = int(input('Sua escolha: '))

    while True: 
        try:
            n1 = int(input('Qual o primeiro número para a operação? '))
            n2 = int(input('Qual o segundo número para a operação? '))
        except ValueError:
            print('Você digitou um valor invalido!')
            continue
        else:
            break

    if choice != 5 and (choice > 0 and choice < 5):
        resposta = calculadora(choice, n1,n2)
        print(f'O resultado para esta operação foi {resposta}.')
    elif choice == 5:
        break