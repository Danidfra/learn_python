from time import sleep;

lista_jogadores = []

while True:
    print('-+-'*20)

    jogador = dict()
    tot_gols = 0

    nome = jogador["nome"] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {nome} jogou? '))

    jogador["partidas"] = partidas
    jogador["gols"] = list()

    for i in range(0, partidas):
        qnt_gols = int(input(f'Quantos gols na {i + 1}ª partida? '))
        jogador["gols"].append(qnt_gols)
        tot_gols += qnt_gols

    jogador["totGols"] = tot_gols
    lista_jogadores.append(jogador)

    continuar = input('Gostaria de adicionar outro jogador? S/N ').strip().lower()

    while continuar not in 'sn':
        print('Opção inválida!')
        continuar = input('Gostaria de adicionar outro jogador? S/N ').strip().lower()

    if continuar in 'n':
        break

print('-+-'*20)

print(f'\033[4m{'Cod':4}|{'Nome':14}|{'Part'}|{'Tot Gols'}')
for c, i in enumerate(lista_jogadores):
    print(f'{(c + 1):4}|{i["nome"]:14}|{i["partidas"]:4}|{i["totGols"]:8}\033[m')
    
print('-+-'*20)

mostrarDados = input('Gostaria de ver os dados dos gols de algum jogador com mais detalhes? S/N ').strip().lower()

if mostrarDados in 'Ss':
    while True: 
        nmr_jogador = int(input('Digite aqui o codigo do jogador: ')) - 1

        print('-+-'*20)
        print(F'Dados do jogador {lista_jogadores[nmr_jogador]["nome"]}:')

        for c, i in enumerate(lista_jogadores[nmr_jogador]["gols"]):
            print(f'No {c+1}º jogo fez {i} gols.')

        continuar = input('Gostaria de ver os gols de outro jogador? S/N ').strip().lower()

        while continuar not in 'sn':
            print('Opção inválida!')
            continuar = input('Gostaria de ver os gols de outro jogador? S/N ').strip().lower()

        if continuar in 'n':
            break

sleep(1)
print('<<< ENCERRANDO PROGRAMA >>>')
sleep(1)

for i in range(3,0, -1):
    print(i,'.'*i)
    sleep(1)

print('<<< PROGRAMA ENCERRADO >>>')