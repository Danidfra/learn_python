

def ficha(nome = 'desconhecido', gols = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome_jogador = input('Nome do Jogador: ')
gols_jogador = input('Número de gols: ')

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador == '':
    jogador = ficha(gols=gols_jogador)
else:
    jogador = ficha(nome_jogador, gols_jogador)


print(jogador)