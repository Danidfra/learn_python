from func.calculator.operators import *

def calculadora(c, n1=0, n2=0):
    if c == 1:
        r = som(n1,n2)
        return r
        
    elif c == 2:
        r = sub(n1,n2)
        return r

    elif c == 3:
        r = mult(n1,n2)
        return r

    elif c == 4:
        r = div(n1,n2)
        return r