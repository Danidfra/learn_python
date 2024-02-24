frase = input('Digite aqui sua frase: ').strip()

frase_l = frase.lower()

lista = list(frase_l)
lista.reverse()


contagem_a = frase_l.count('a')
pI = frase_l.find('a')
pF = frase_l.rfind('a')

print(f'A letra "A" aparece {contagem_a} vezes na frase. ')
print(f'A primeira letra "A" apareceu na {pI + 1}˚ posição.')
print(f'A última letra "A" apareceu na {pF + 1}˚ posição.')
