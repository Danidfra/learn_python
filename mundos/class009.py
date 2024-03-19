# Tratamento de cadeias textos 

# Fatiamento

frase = "Finalmente estou quase conseguindo um estagio rsrs."
frase_len = len(frase)
frase_count = frase.count('a', 0, 20)
frase_find = frase.find(' um')

frase_test_boolean = "na Apple" in frase
work = "na Apple."

print(frase_test_boolean)


frase_right = frase.replace(frase[11:34], "consegui")
frase_wish = frase_right.replace(frase_right[31:], work)

frase_dividida = frase_wish.split()

teste = ' '.join(frase_dividida)

print(frase_dividida)
print(teste)
