from time import sleep;

start = input('Vamos iniciar nossos calculos? S/N ').lower().strip()

while start != 's' and start != 'n':
    print('Opção inválida')
    start = input('Digite novamente sua resposta. Quer realizar algum calculo? S/N ').lower().strip()

if start == 's':
    continuar = True
elif start == 'n':
    continuar = False


while continuar == True:
    nmr_0 = float(input('Digite o primeiro número: '))
    nmr_1 = float(input('Digite o primeiro número: '))

    print('\n', '-'*5, 'Opções', '-'*5, '\n')
    escolha = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nResposta: '))

    while escolha < 1 or escolha > 5:
        print('\n', '-'*5, 'Opção inválida', '-'*5, '\n')
        escolha = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nResposta: '))
        

    if escolha == 1:
        soma = nmr_0 + nmr_1
        print(f'A soma dos valores: {nmr_0} e {nmr_1} é igual a {soma}.')

    elif escolha == 2:
        resultado_multiplicacao = nmr_0 * nmr_1
        print(f'A multiplicação dis valores: {nmr_0} e {nmr_1} é igual a {resultado_multiplicacao}.')

    elif escolha == 3:
        if nmr_0 > nmr_1:
            print(f'O número {nmr_0} é o maior.')
        elif nmr_0 < nmr_1:
            print(f'O número {nmr_1} é o maior.')
        else:
            print('Os números são iguais, por tanto não existe um número maior.')
    elif escolha == 5:
        continuar = False


    if escolha != 4 and escolha != 5:
        print('\nIniciando proximo calculo', '\n')
        sleep(2)

print('Programa finalizado... Caso queira realizar novas operações sabe onde me achar.')