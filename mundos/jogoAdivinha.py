import random;

def pergunta_dica(x, z):
    pergunta_dica = input('Quer uma dica? S/N ').lower().strip()

    if pergunta_dica == 's':
        if x > z:
                print('Seu palpite está acima do número correto.')
        elif x < z:
                print('Seu palpite está abaixo do número correto.')


def testa_resposta(x, z, y):
    if x == z:
        print('Parabéns, você acertou!')
    else:

        if y > 1:
            y -= 1
            print(f'Que pena, você errou! Você possui mais {y} tentativas.')

            pergunta_dica(x, z)

            x = int(input('Tente novamente. Qual foi o número que pensei: '))
            testa_resposta(x, z, y)
        else:
            
            reiniciar_jogo = input('Que pena, você errou! Você não possui mais nenhuma tentativa. Gostaria de reiniciar o jogo? S/N ').lower().strip()

            if reiniciar_jogo == 's':
                 jogo_adivinha()
            elif reiniciar_jogo == 'n':
                print('Tchau tchau, caso queira participar sabe onde me encontrar!')

def jogo_adivinha():
    nmr_tentativas = 3
    nmr_aleatorio = random.randint(1, 10)

    resposta_1 = int(input('Eu pensei em um número aleatorio de 0 a 10... Tente adivinhar qual foi o número que pensei: '))

    testa_resposta(resposta_1, nmr_aleatorio, nmr_tentativas)

resposta_usuario = input('Gostaria de participar de um jogo de advinhação? S/N ').lower().strip()



if resposta_usuario == 's':
    print('Otimo, vamos iniciar o jogo.')
    jogo_adivinha()

elif resposta_usuario == 'n':
    print('Tchau tchau, caso queira participar sabe onde me encontrar!')

