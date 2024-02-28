
sexo = input('Digite o seu sexo: M/F ').lower().strip()
print(sexo)

while sexo != 'm' and sexo != 'f':
    sexo = input('Você digitou um sexo que não esta nas opções. Digite o seu sexo: M/F ').lower().strip()
    print(sexo)
