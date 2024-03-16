

def ficha(nome = 'convidado', gols = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome_jogador = input('Nome do Jogador: ')

# print(nome_jogador)
# print(gols_jogador)

jogador = ficha()

print(jogador)