def obt_name():
    quest_1 = (input('Olá, poderia me fornecer seu nome completo? s/n ')).lower()

    if quest_1 == 's':
        fullname = input('Otímo, qual é seu nome completo? ')
    elif quest_1 == 'n':
        quest_2 = (input('Que pena, gostaria de te falar algumas informações sobre ele... Tem certeza que não quer falar o seu nome completo? s/n ')).lower()
        if quest_2 == 's':
            print('Ok, eu respeito sua opção, obrigado por seu tempo, caso mude de ideia depois sabe onde me encontrar!! ')
        else:
            fullname = input('Otímo, qual é seu nome completo? ')

    else:
        print('Você não respondeu nada... Vamos tentar novamente. ')
        obt_name()
            
    return fullname


fName = obt_name()

# Nome em maiúsculo
upperName = fName.upper()

# Nome em minúsculo
lowerName = fName.lower()

# Contagem de letras (sem os espaços)
cName = fName.split()
jName = ''.join(cName)
countName = len(jName)

# Contagem de letras (sem os espaços)
cFName = len(cName[0])


print(upperName)
print(lowerName)
print(countName)
print(cFName)