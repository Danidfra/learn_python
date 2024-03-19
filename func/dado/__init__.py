def leiaDinheiro(p):

    inp = input(p).strip()
    n = inp.replace(',','.')
    test = n.replace('.','')

    if test.isnumeric():
        return float(n)
    else:
        while not test.isnumeric():
            print('Erro! ')
            inp = input(p).strip()
            n = inp.replace(',','.')
            test = n.replace('.','')
        
        return float(n)
    
