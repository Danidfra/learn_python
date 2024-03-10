from random import randint;

lista_jogador = list()
jogador = {}

qnt_jogadores = int(input('Quantos jogadores irão participar? '))

for i in range(0, qnt_jogadores):
    jogador["nome"] = input(f'Qual o nome do {i + 1}º jogador? ')

    nmr = randint(1, 6)
    
    jogador["resultado"] = nmr
    print(jogador)
    
    if i > 0:
        for c, j in enumerate(lista_jogador):
            if j["resultado"] > jogador["resultado"] or j["resultado"] == jogador["resultado"]:
                print('aqui 1')
                lista_jogador.insert(c, jogador.copy())
                break
            elif c == (len(lista_jogador) - 1):
                lista_jogador.append(jogador.copy())
    else:                
        lista_jogador.append(jogador.copy())

    print(lista_jogador)


print(lista_jogador)