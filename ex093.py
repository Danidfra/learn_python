jogador = dict()

jogador["nome"] = input('Nome do Jogador: ')

qnt_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador["partidas"] = qnt_partidas

for i in range(0, qnt_partidas):
    qnt_gols = int(input(f'Quantos gols na {i + 1}ª partida? '))