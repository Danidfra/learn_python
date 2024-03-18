from random import randint;
from operator import itemgetter;
lista_jogador = {}
jogador = {}

qnt_jogadores = int(input('Quantos jogadores irão participar? '))
print('-'*60)

for i in range(0, qnt_jogadores):
    jogador["nome"] = input(f'Qual o nome do {i + 1}º jogador? ')

    nmr = randint(1, 6)
    
    jogador["resultado"] = nmr
    
    lista_jogador[f"jogador{i}"] = jogador.copy()

print(lista_jogador)

print('-+-'*20)
print('Valores sorteados: ')
for c, i in enumerate(lista_jogador.values()):
    print(f' - {i["nome"]} tirou {i["resultado"]} no dado.')
print('-+-'*20)

print('  == RANKING DOS JOGADORES ==  ')

ranking = sorted(lista_jogador.values(), key=lambda x: x["resultado"], reverse=True)


for posicao, jogador in enumerate(ranking, start=1):
    print(f'{posicao}º lugar: {jogador["nome"]} com resultado {jogador["resultado"]}')