from func.wb import whileBreaker;
lista_convidados = []
qnt_convidados = 0

continuar = True
while continuar:
    convidado = dict()
    convidado["nome"] = input('Qual o nome do convidado? ')
    lista_convidados.append(convidado)
    qnt_convidados += 1

    if qnt_convidados == 1:
        print(f'Você adicionou um convidado. Ate o momento temos apenas {qnt_convidados} convidado.')
    else:
        print(f'Você adicionou um convidado. Ate o momento temos {qnt_convidados} convidados.')
    continuar = whileBreaker()

# for c,i in enumerate(lista_convidados):

lista_convidados.sort(key=lambda value: value["nome"])

print(f'Os convidados listados em ordem alfabetica são:')
for i in lista_convidados:
    print(f' - {i["nome"]}')

print(f'Ao todo teremos {qnt_convidados} convidados na festa.')