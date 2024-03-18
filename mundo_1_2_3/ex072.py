# teste_0 = 'Hani', 'Dani', 'Aninha', 'Oculos'
    # teste_1 = 'Daniel Filemon'

    # print(teste_0)
    # print(teste_0[0])
    # print(teste_0[1])
    # print(teste_0[2])
    # print(teste_0[3])
    # print(teste_0[-1])
    # print(teste_0[-2])
    # print(teste_0[-3])
    # print(teste_0[-4])


cont_valores = 0

while True:

    nmr_extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

    nmr_entrada = int(input('Digite um número de 1 a 20 e vou lhe informar como é a sua forma por extenso: '))

    while nmr_entrada < 1 or nmr_entrada > 20:
        nmr_entrada = int(input('Valor invalido. Por favor informe um número de 1 a 20: '))

    cont_valores += 1

    print(f'Voce digitou {nmr_entrada}, esse número por extenso se escreve assim: {nmr_extenso[nmr_entrada].title()}')


    pergunta_continuar = input('Quer continuar? S/N: ').lower().strip()

    while pergunta_continuar != 's' and pergunta_continuar != 'n':
        pergunta_continuar = input('Opção inválida. Quer continuar? S/N: ').lower().strip()

    if pergunta_continuar == 'n':
        break

print(f'Fim do programa. Foi convertido para extenso um total de {cont_valores} valores. Caso queira informar mais valores sabe onde me achar... Até breve!! ')