jogador = dict()

nome = jogador["nome"] = input('Nome do Jogador: ').strip().title()


qnt_partidas = int(input(f'Quantas partidas {nome} jogou? '))
jogador["partidas"] = qnt_partidas

lista_gols = []
total_gols = 0

for i in range(0, qnt_partidas):
    qnt_gols_partida = int(input(f'Quantos gols na {i + 1}ª partida? '))

    lista_gols.append(qnt_gols_partida)
    total_gols += qnt_gols_partida

jogador["totalGols"] = total_gols
jogador["gols"] = lista_gols

print('-+-'*20)
print(jogador)
print('-+-'*20)
print(f'O jogador se chama {nome}.')
print(f'O {nome} jogou {jogador["partidas"]} partidas e seu historico de gols foi:')
for c, i in enumerate(jogador["gols"]):
    print(f' - Na {c + 1}ª partida fez {i} gols.')

print(f'O {nome} fez um total de {jogador["totalGols"]} gols.')