cidade = (input('Digite o nome da sua cidade: ')).lower()

re = cidade.split()

if re[0] == 'santos':

    print('Sua cidade começa com Santos. ')

else: 
    print('Sua cidade não começa com Santos. ')