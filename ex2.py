from func.title import Tabela
from time import sleep

def pp(palavra):
    for c,i in enumerate(lista_palavras):
        if palavra == i[0]:
            return True, c
        
    return False, -1
    

opc_tabela = ('Pesquisar palavra', 'Ver todas as palavras cadastradas', 'Cadastrar nova palavra', 'Sair do Sistema')

tabela = Tabela( 60, opc_tabela)

while True:
    sleep(1)
    tabela.montar('Dicionário')

    try:
        choice = int(input('Sua opção: '))
    except ValueError:
        print('Opção invalida!')
        continue

    if choice == 1 or choice == 2:
        with open('dicionario.txt', 'r') as ler:
            infos = ler.read()

            lista_palavras = list(infos.split(';'))
            for c,i in enumerate(lista_palavras):
                lista_palavras[c] = i.split('%')

            if choice == 1:
                tabela.montar('Procurar Palavra', tab=False)
                while True:
                    procurar_palavra = input('Gostaria de procurar qual palavra? ')
                    choice_certa = input(f'Você quer procurar pela palavra {procurar_palavra} correto? S/N ').strip().lower()
                    sleep(0.5)
                    tabela.montar(f'Procurando <<{procurar_palavra}>>', tab=False)
                    sleep(1)
                    if choice_certa in 's':
                        encontrado, pos = pp(procurar_palavra)
                        if encontrado:
                            sleep(1)
                            print(f'{lista_palavras[pos][0]:14}{lista_palavras[pos][1]}')
                        else:
                            sleep(1)
                            print(f'A palavra "{procurar_palavra}" não foi encontrada')
                        break

            if choice == 2:
                tabela.montar('Palavras cadastradas', tab=False)
                print()
                for i in (infos.split(';')):
                    i = i.split('%')
                    for c,j in enumerate(i):
                        if c == 0:
                            sleep(1)
                            print(f'{j:14}', end='')
                        elif c == 1:
                            sleep(1)
                            print(f'{j}')
                sleep(1)
                print()


    if choice == 3:
        tabela.montar('Cadastro', tab=False)
        palavra = dict()
        palavra["palavra"] = input('Informe a palavra que gostaria de cadastrar: ')
        palavra["significado"] = input('Informe o significado da palavra: ')

        with open('dicionario.txt', 'a+') as gravar:
            for c,i in enumerate(palavra.values()):
                if c == 0:
                    gravar.write(f'{i}%')
                else:
                    gravar.write(f'{i};')

    elif choice == 4:
        break


