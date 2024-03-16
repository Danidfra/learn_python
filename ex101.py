from datetime import datetime;

def testaIdade(i):
    """
    -> Função criada para conferir o status para votar:
    :param i: idade
    :return: retorna o status do voto
    """
    if i < 16:
        return 'NEGADO'
    elif i < 18:
        return 'OPCIONAL'
    elif i < 65:
        return 'OBRIGATÓRIO'
    if i >= 65:
        return 'OPCIONAL'

def voto(a):
    """"
    -> Função para calcular a idade e criar uma frase informando informando o status do voto:
    :param a: ano de nascimento
    :return: retorna a frase contendo o status do voto
    """
    ano_atual = datetime.now().year
    age = ano_atual - a

    resposta = testaIdade(age)

    return f'Com {age} anos: VOTO ' + resposta

# PROGRAMA PRINCIPAL

try:
    ano_nas = int(input('Em que ano você nasceu? '))
except ValueError:
    print('Digite um valor númerico... ')
    ano_nas = int(input('Em que ano você nasceu? '))

print(voto(ano_nas))