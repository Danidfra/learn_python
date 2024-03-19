

def soma_pares(qnt_nmr_somar, soma, qnt_nmr, qnt_nmr_contados):
    for i in range(0, qnt_nmr_somar):
        qnt_nmr += 1
        nmr = int(input('Digite um número: '))
        if nmr % 2 == 0:
            soma += nmr
            qnt_nmr_contados += 1
    
    return soma, qnt_nmr, qnt_nmr_contados

def soma_impares(qnt_nmr_somar, soma, qnt_nmr, qnt_nmr_contados):
    for i in range(0, qnt_nmr_somar):
        qnt_nmr += 1
        nmr = int(input('Digite um número: '))
        if nmr % 2 != 0:
            soma += nmr
            qnt_nmr_contados += 1

    return soma, qnt_nmr, qnt_nmr_contados

def testa_tipo(tipo, soma, qnt_nmr, qnt_nmr_contados):
    if tipo == 'pares':
        soma, qnt_nmr, qnt_nmr_contados = soma_pares(qnt_nmr_somar, soma, qnt_nmr, qnt_nmr_contados)
        return soma, qnt_nmr, qnt_nmr_contados, tipo

    elif tipo == 'impares':
        soma, qnt_nmr, qnt_nmr_contados = soma_impares(qnt_nmr_somar, soma, qnt_nmr, qnt_nmr_contados)
        return soma, qnt_nmr, qnt_nmr_contados, tipo
    else:
        tipo_nov = input('Você não informou corretamente se queria a soma dos pares ou impares.\nPoderia me responder novamente se quer somar os números pares ou os impares? Pares/Impares ')
        soma, qnt_nmr, qnt_nmr_contados, tipo = testa_tipo(tipo_nov, soma, qnt_nmr, qnt_nmr_contados)
        return soma, qnt_nmr, qnt_nmr_contados, tipo_nov


qnt_nmr_somar = int(input('Quantos números você gostaria de somar? ')) 
tipo_soma = input('Você gostaria que eu somasse somente os pares ou impares? pares/impares ').lower().strip()

soma = 0
qnt_nmr = 0
qnt_nmr_contados = 0

s, qn, qnc, t = testa_tipo(tipo_soma, soma, qnt_nmr, qnt_nmr_contados)
    

print(f'Você informou {qn}, dos quais {qnc} foram adicionados a soma. Apos fazer o calculo a soma dos números {t} deu {s}. ')