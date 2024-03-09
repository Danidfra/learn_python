import datetime;

data_ano = datetime.date.today().year

cp = dict()

cp["nome"] = input('Nome: ')
cp["idade"] = data_ano - int(input('Ano de Nascimento: '))
cp["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))

if cp["ctps"] != 0:
    cp["contratacao"] = int(input('Ano de contratação: '))
    cp["salario"] = float(input('Salário: '))
    cp["aposentadoria"] = cp["idade"] + (35 - (data_ano - cp["contratacao"]))

    print(f'Esta pessoa se chama {cp["nome"]}, tem {cp["idade"]} anos e possui os seguintes dados em sua carteira de trabalho:\n - Nº {cp["ctps"]}\n - Foi contratado no ano de {cp["contratacao"]}\n - Seu salário é de R${cp["salario"]:.2f}\n - Irá se aposentar com {cp["aposentadoria"]} anos')

else:
    print(f'O {cp["nome"]}, tem {cp["idade"]} anos e não possui carteira de trabalho.')