conjunto_nmr = list()

while True:
    nmr = int(input('Digite um valor: '))
    if nmr not in conjunto_nmr: 
        conjunto_nmr.append(nmr)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado! Não vou adicionar... ')

    continuar = input('Quer continuar? S/N ')
    while continuar not in 'SssimSimNnnãoNãonaoNao':
            print('Opção invalida...')
            continuar = input('Quer continuar? S/N ')

    if continuar in 'NnnãoNãonaoNao':
        print('-='*40)
        break

conjunto_nmr.sort()

print(f'Você digitou os valores {conjunto_nmr}')