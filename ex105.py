
def somaNotas(n):
    """"
    -> Função para somar as notas.
    :param n: lista com as notas.
    :return: retorna a soma das notas no formato float.
    """
    soma = 0
    for i in n:
        soma += i
    return soma

def verificaStatus(m):
    """"
    -> Função para verificar o status da turma.
    :param m: media da turma.
    :return: retorna a situação da turma no formato de string.
    """
    if m >= 7:
        s = 'BOA'
    elif m >= 6:
        s = 'RAZOÁVEL'
    else:
        s = 'RUIM'
    return s

def notas(n, sit):
    """"
    -> Função para analisar notas. 
    :param n: lista contendo uma ou mais notas dos alunos (aceita várias)
    :param sit: (valor opcional) indica se deve ou não adicionar a situação
    :return: retorna um dicionário com várias informações sobre a turma.
    """
    dn = {}
    dn["total"] = qnt_notas = len(n)
    dn["maior"] = max(n)
    dn["menor"] = min(n)

    soma_notas = somaNotas(n)
    dn["média"] = media = float('{:.2f}'.format(soma_notas/qnt_notas))
    print(type(media), 'teste aqui')
    if sit:
        dn["situação"] = status = verificaStatus(media)

    return dn

def date_inputs():

    list_notas = []

    while True:
        nmr = float(input('Informe a nota a ser adicionada: '))
        list_notas.append(nmr)

        continuar = input('Quer adicionar outra nota? S/N ').strip().lower()

        while continuar not in 'sn':
            print('Opção invalida!')
            continuar = input('Quer adicionar outra nota? S/N ').strip().lower()

        if continuar in 'n':
            break

    return list_notas

# x = True if input('Gostaria de saber sobre a situação da turma? S/N ').lower().strip() in 's' else False
# print(x)
list_n = date_inputs()
dic_notas = notas(list_n, sit=True)

print(dic_notas)