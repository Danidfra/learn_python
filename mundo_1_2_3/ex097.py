from time import sleep;

# Criando função
def formata_titulo(frase):
    print('-'*(len(frase) + 4))
    print(f'  {frase}  ')
    print('-'*(len(frase) + 4))

# PROGRAMA PRINCIPAL
print('  <<< INICIANDO PROGRAMA >>>  ')
sleep(1)

# Adicionando um loop
while True:
    # Chamando a função
    formata_titulo(input('  Qual a frase a ser escrita?  ').strip())

    # Criando possivel ponto final
    continuar = input('  Gostaria de adicionar outra frase? S/N  ').strip().lower()

    while continuar not in 'sn':
        print('  Opção inválida!')
        continuar = input('  Gostaria de adicionar outra frase? S/N  ').strip().lower()

    if continuar in 'n':
        break

sleep(1)
print('  <<< PROGRAMA ENCERRADO >>>  ')