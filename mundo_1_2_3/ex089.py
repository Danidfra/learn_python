from time import sleep;
lista_alunos = []

while True:
    aluno = []
    nome_aluno = input('Nome do aluno: ')
    nota_1 = float(input('Digite a 1ª nota: '))
    nota_2 = float(input('Digite a 2ª nota: '))

    lista_notas = [nota_1, nota_2]

    aluno.append(nome_aluno)
    aluno.append(lista_notas[:])
    lista_alunos.append(aluno[:])

    lista_notas.clear()
    aluno.clear()

    continuar = input('Quer adicionar outro aluno? S/N ')

    while continuar not in 'SsNn':
        print('Opção inválida!')
        continuar = input('Quer adicionar outro aluno? S/N ')

    if continuar in 'Nn':
        break

print('-=-'*20)
print(f'{'Nº':4} {'NOME':13} {'MÉDIA':9}')
print('-'*26)

for c, i in enumerate(lista_alunos):
    sleep(1)
    print(f'{c:>4}',f'{i[0]:15}', f'{(i[1][0] + i[1][1]) / 2}')

print('-'*35)


mostrar_nota = input('Gostaria de conferir a nota de algum dos alunos? S/N ')

if mostrar_nota in 'Ss':
    while True:
        mostrar_aluno = int(input('Mostrar notas de qual aluno? (Digite 999 para encerrar) '))
        if mostrar_aluno == 999:
            break
        else:
            if mostrar_aluno > (len(lista_alunos) - 1) or mostrar_aluno < 0:
                print('Aluno inválido!')
            else:
                print(f'As notas de {lista_alunos[mostrar_aluno][0]} são: ', end='')
                for c, i in enumerate(lista_alunos[mostrar_aluno][1]):
                    if c == (len(lista_alunos[mostrar_aluno][1]) -1):
                        print(f'{i}')
                    else:
                        print(f'{i}, ', end='')

                # for i in lista_alunos:
                # for i in range(0, 1):
                #     for c, j in enumerate(i[1]):
                #         if c == (len(i[1]) - 1):
                #             print(f'{j}')
                #         else:
                #             print(f'{j}, ', end='')


sleep(1)
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')