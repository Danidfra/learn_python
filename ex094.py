from datetime import date;

ano_atual = date.today().year
lista_pessoas = []

while True:
    pessoa = {}
    pessoa["nome"] = input('Nome: ').strip().title()
    pessoa["sexo"] = input('Sexo[M/F]: ').lower()

    while pessoa["sexo"] not in 'mf':
        print('Opção inválida! ')
        pessoa["sexo"] = input('Sexo[M/F]: ').lower()

    # pessoa["idade"] = ano_atual - (int(input('Em que ano você nasceu? ')))
    pessoa["idade"] = (int(input('Idade:')))

    lista_pessoas.append(pessoa.copy())

    continuar = input('Quer adicionar outra pessoa? S/N ')

    while continuar not in 'SsNn':
        print('Opção inválida! ')
        continuar = input('Quer adicionar outra pessoa? S/N ')

    if continuar in 'Nn':
        break

total_idades = 0
for i in lista_pessoas:
    total_idades += i["idade"]

media_idade = total_idades / len(lista_pessoas)

print('-+-'*20)
print(lista_pessoas)
print('-+-'*20)
print(f'A) Foram cadastradas um total de {len(lista_pessoas)} pessoas.')
print(f'\nB) A media de idade do grupo é {media_idade}.')
print(f'\nC) As mulheres do grupo são:')
for c, i in enumerate(lista_pessoas):
    if i["sexo"] == 'f':
        print(f' - {i["nome"]}.')
    # if c == 0:
    #     print(f'\nD) As pessoas acima da média de idade são:')
    #     if i["idade"] > media_idade:
    #         print(f' - {i["nome"]} com {i["idade"]} anos.')
    # else:
    #     if i["idade"] > media_idade:
    #         print(f' - {i["nome"]} com {i["idade"]} anos.')
        

print(f'\nD) As pessoas acima da média de idade são:')
for i in lista_pessoas:
    if i["idade"] > media_idade:
        print(f' - {i["nome"]} com {i["idade"]} anos.')
print('-+-'*20)
    