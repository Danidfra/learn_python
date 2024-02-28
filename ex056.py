qnt_pessoas = int(input('Quantas pessoas vão participar dessa pesquisa? '))


media_idade = 0
contador_media = 0
mais_velho = 0
nome_homem_velho = ''
qnt_mulheres = 0



for i in range(0, qnt_pessoas):
    print('-'*5, ' ' , i + 1,'ª PESSOA ', '-'*5)
    name = input('Nome: ')
    age = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower().strip()

    if i == 0:
        soma_idade = age
        contador_media = 1
        
        if sexo == 'm':
            nome_homem_velho = name
            mais_velho = age
        if sexo == 'f':
            if age < 20:
                qnt_mulheres += 1
    elif i < qnt_pessoas -1:
        soma_idade += age
        contador_media += 1

        
        if sexo == 'm':
            if age > mais_velho:
                nome_homem_velho = name
                mais_velho = age
        if sexo == 'f':
            if age < 20:
                qnt_mulheres += 1
    else:
        soma_idade += age
        contador_media += 1
        media_idade = (soma_idade / contador_media)

        if sexo == 'm':
            if age > mais_velho:
                nome_homem_velho = name
                mais_velho = age
        if sexo == 'f':
            if age < 20:
                qnt_mulheres += 1


print(f'A média de idade do grupo é de {media_idade}.')
print(f'O homem mais velho tem {media_idade} anos e se chama {nome_homem_velho}.')
print(f'Ao todo são {qnt_mulheres} mulheres com menos de 20 anos.')



        
        


