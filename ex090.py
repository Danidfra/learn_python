lista_alunos = []
aluno = dict()

while True:
    aluno["nome"] = input('Qual o nome do aluno? ')
    aluno["sexo"] = input('Qual o genero do aluno? M/F ')
    if aluno["sexo"] not in 'MmFf':
        print('Opção inválida!')
        aluno["sexo"] = input('Qual o genero do aluno? M/F ')

    nota_1 = float(input('Qual a primeira nota? '))
    nota_2 = float(input('Qual a segunda nota? '))
    
    media = (nota_1 + nota_2) / 2
    aluno["media"] = media

    if media >= 7:
        aluno["status"] = 'aprovou'
    elif media >= 5:
        aluno["status"] = 'está em recuperação'
    else:
        aluno["status"] = 'reprovou'

    lista_alunos.append(aluno.copy())

    continuar = input('Quer adicionar outro aluno? S/N ')
    while continuar not in 'SsNn':
        print('Opção inválida!')
        continuar = input('Quer adicionar outro aluno? S/N ')
    
    if continuar in 'Nn':
        break
    


for i in lista_alunos:
    if i["sexo"] in 'Mm':
        print(f'O aluno {i["nome"]} teve a media de {i["media"]} pontos e {i["status"]}.')
    elif i["sexo"] in 'Ff':
        print(f'A aluna {i["nome"]} teve a media de {i["media"]} pontos e {i["status"]}.')