from time import sleep;
from random import randint;


print('Seja bem vindo!! ')
resposta_jogar = input('Você gostaria de jogar Jokenpô? S/N ').lower().strip()

def start_jogo():
    print('Deixe-me pensar... ')
    sleep(1)
    print('Ja decidi qual vou escolher hehe...')
    sleep(1)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)

def valida_resposta_jogador(rj):
    if rj != 'pedra' and rj != 'papel' and rj != 'tesoura':
        rj = input('O jogador não inseriu uma resposta valida.\nPoderia me informar sua resposta novamente? Pedra/Papel/Tesoura ').lower().strip()
        rj = valida_resposta_jogador(rj)
        return rj
    elif rj == 'pedra' or rj == 'papel' or rj == 'tesoura':
        return rj


def escolha_computador():
    nmr = randint(1, 3)
    if nmr == 1:
        return 'pedra'
    elif nmr == 2:
        return 'papel'
    elif nmr == 3:
        return 'tesoura'


def testa_respostas(rc, rj):

    if rc == 'pedra' and rj == 'papel':
        return 'Parabéns você venceu!'

    elif rc == 'papel' and rj == 'tesoura':
        return 'Parabéns você venceu!'

    elif rc == 'tesoura' and rj == 'pedra':
        return 'Parabéns você venceu!'

    elif rc == 'pedra' and rj == 'tesoura':
        return 'Eu venci!'

    elif rc == 'papel' and rj == 'pedra':
        return 'Eu venci!'

    elif rc == 'tesoura' and rj == 'papel':
        return 'Eu venci!'

    elif rc == rj:
        return 'Empatou!'


def jogo_jokenpo():
    
    start_jogo()

    resposta_computador = escolha_computador()

    resposta_jogador = input('Qual você vai escolher? Pedra/Papel/Tesoura ').lower().strip()
    resposta_jogador_validada = valida_resposta_jogador(resposta_jogador)


    
    resultado = testa_respostas(resposta_computador, resposta_jogador_validada)

    print(f'{resultado} Eu escolhi {resposta_computador}.')

if resposta_jogar =='s':
    jogo_jokenpo()
else:
    print('Tchau tchau, caso queira jogar sabe onde me encontrar!')