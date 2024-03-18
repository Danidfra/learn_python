# from moeda


def leiaDinheiro(p):

    n = input(p)

    if n.isnumeric():

        return float(n)
    else:
        while not n.isnumeric():
            print('Erro! ')
            n = input('Digite o preço: R$')
        
        return float(n)
    
