
def somar_intervalo():
    nmr_i = int(input('Qual o número inicial? '))
    nmr_f = int(input('Qual o número final? '))

    tipo = input('Gostaria que fosse somado os números pares ou impares? Pares/Impares ').lower().strip()

    s = 0
    if tipo == 'pares':    
        for c in range(nmr_i, nmr_f):
            if c % 2 == 0:
                if c % 3 == 0:
                    s += c
        return s
    elif tipo == 'impares':
        for c in range(nmr_i, nmr_f):
            if c % 2 != 0:
                if c % 3 == 0:
                    s += c
        return s



print('Olá espero que esteja bem!! Vou realizar uma soma, com somente os números que são múltiplos de três... \nPoderia me informar os números para a contagem? ')

resultado = somar_intervalo()

print(resultado)