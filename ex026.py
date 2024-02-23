frase = input('Digite aqui sua frase: ')

frase_l = frase.lower()

lista = list(frase_l)
lista.reverse()

print(lista)

contagem_a = frase_l.count('a')
contagem_espaços = frase_l.count(' ')
pI = frase_l.find('a')
pF = ''
frase_cortada = frase_l.split()
tamanho_lista = len(frase_cortada)

for i in lista:
    if i == 'a':
        q_total = len(lista) - i
        pF = q_total - 1
        print(lista[pF])
        break
