from random import randint;
from time import sleep;


start = input('Quer brincar de tentar adivinhar o número que estou pensando? S/N: ').lower().strip()

if start == 's':
    continuar_jogando = True

    while continuar_jogando == True:
        print('Ok deixe-me pensar em um número...')
        sleep(randint(1, 7))
        print('hmmm...')
        sleep(randint(2, 10))
        
        nmr_computador = randint(1, 10)
        tot_respostas = 0
        respostas_erradas = 0

        resposta = int(input('Prontinho rsrs... Eu pensei em um número de 1 a 10 e você tem que adivinhar qual número foi...\nEm que número eu pensei? '))
        tot_respostas += 1
        while resposta != nmr_computador:
            tot_respostas += 1
            respostas_erradas += 1
            resposta = int(input('Você errou tente novamente...\nEm que número eu pensei? '))

        print(f'Parabéns você acertou!! Você tentou {tot_respostas} vez(es) e errou {respostas_erradas} vez(es). ')

        continuar = input('Quer jogar novamente? S/N: ').lower().strip()
        
        if continuar == 'n':
            continuar_jogando = False
            print('Obrigado pela brincadeira, tchau tchau!! ')

else:
    print('Ok, caso queira brincar sabe onde me achar!')


