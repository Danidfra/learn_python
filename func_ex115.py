def mostrarPessoa():
    lista_pessoas = []
    with open('teste.txt', 'r') as ler:
        dados = ler.read()

        infos_pessoa=dados.split('/')

        for c,i in enumerate(infos_pessoa):
            if i == '' :
                infos_pessoa.pop(c)
            else:
                pessoa = {}
                lista_infos = i.split(',')

                pessoa["nome"] = lista_infos[0]
                pessoa["idade"] = lista_infos[1]

                lista_pessoas.append(pessoa)

    for i in lista_pessoas:
        print(f'{i["nome"]:40}{i["idade"]:>2} anos')


def adicionarPessoa():
    from datetime import datetime;

    ano = datetime.now().year

    lista_pessoas = []

    continuar = True

    while continuar:
        pessoa = {}
        pessoa["nome"] = input('Nome: ')
        while True:
            try:
                pessoa["idade"] = ano - int(input('Ano de Nascimento: '))
            except ValueError:
                print('ERRO! Por favor, digite um número inteiro válido.')
            else:
                break

        lista_pessoas.append(pessoa)

        continuar = input('Gostaria de adicionar outra pessoa? S/N  ').strip().lower()

        while continuar not in 'sn':
            print('Opção inválida!')
            continuar = input('Gostaria de adicionar outra pessoa? S/N  ').strip().lower()

        if continuar in 'n':
            continuar = False
        elif continuar in 's':
            continuar = True

    with  open('teste.txt', 'a') as gravar:
        for c, i in enumerate(lista_pessoas):
            gravar.write('%s,' % i["nome"])
            gravar.write('%s/' % i["idade"])

    print('Novos registros adicionados com sucesso.')

