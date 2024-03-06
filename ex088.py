from time import sleep;
from random import randint;

print('-'*30)
print(f'{'JOGO MEGA SENA':^30}')
print('-'*30)

qnt_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

lista_jogos = list()
jogo = list()

for i in range(0, qnt_jogos):
    cj = 0
    while cj < 6:
        nmr_sorteado = randint(1, 60)
        if nmr_sorteado not in jogo:
            jogo.append(nmr_sorteado)
            cj += 1
    
    jogo.sort()
    lista_jogos.append(jogo[:])
    jogo.clear()


print('-=-'*2, F'SORTEANDO {qnt_jogos} JOGOS', '-=-'*2)

for c, i in enumerate(lista_jogos):
    sleep(0.5)
    print(f'Jogo {c + 1}: ', end='')
    for d, j in enumerate(i):
        if d == (len(i) - 1):
            print(f'{j} ')
        else:
            print(f'{j} ', end='')

print('-=-'*2, '< BOA SORTE! >', '-=-'*2)



# TESTING:


# jogo = list()
# c = 0


# while c <10:
#     print(jogo)
#     nmr_sorteado = randint(1, 10)
#     if str(nmr_sorteado) not in jogo:
#         jogo.append(str(nmr_sorteado))
#         c += 1


# jogo.sort()
# print(jogo)