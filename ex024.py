cidade = input('Digite o nome da sua cidade: ').lower().strip()

re = cidade.split()

if re[0] == 'santo':

    print('Sua cidade começa com Santo. ')

else: 
    print('Sua cidade não começa com Santo. ')