expr = input('Digite a expressão: ')

list_p = list()

for i in expr:
    if i == '(':
        list_p.append('(')
    elif i == ')':
        if len(list_p) > 0:
            list_p.pop()
        else:
            list_p.append(')')
            break
    
if len(list_p) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')