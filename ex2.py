from func.title import Tabela

opc_tabela = ('Pesquisar palavra', 'Ver todas as palavras cadastradas', 'Cadastrar nova palavra', 'Sair do Sistema')

while True:
    tabela = Tabela('Dicionário', 50, opc_tabela)

    tabela.montarTabela()

    choice = int(input('Sua opção: '))

    if choice == 1 or choice == 2:
        with open('dicionario.txt', 'r') as ler:
            if choice == 1:
                procurar_palavra = input('Gostaria de procurar qual palavra? ') 
                choice_certa = input(f'Você quer procurar pela palavra {procurar_palavra} correto? S/N ').strip().lower()
                if choice_certa in 's':
                    print('finalizei aqui')
                    break
                



    if choice == 2:
        palavra = dict()
        palavra["palavra"] = input('Informe a palavra que gostaria de cadastrar: ')
        palavra["significado"] = input('Informe o significado da palavra: ')

        with open('dicionario.txt', 'a+') as gravar:
            for c,i in enumerate(palavra.values()):
                if c == 0:
                    gravar.write(f'{i},')
                else:
                    gravar.write(f'{i}/')

    elif choice == 3:
        break


