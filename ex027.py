nome = input('Digite seu nome completo: ').strip()

nomeFormatado = nome.split()

print(f'Seu primeiro nome é ', nomeFormatado[0].title())
print(f'Seu último nome é ', nomeFormatado[len(nomeFormatado) - 1].title())