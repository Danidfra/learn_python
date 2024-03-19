from func_ex115 import mostrarPessoa, adicionarPessoa
from func.title import formaTitulo

def escolha(op):
    if op == 1:
        formaTitulo('PESSOAS CADASTRADAS', 50)
        mostrarPessoa()
        return True
    elif op == 2:
        adicionarPessoa()
        return True
    elif op == 0:
        resp = False
        return resp
    else:
        return False, 'teste'


continuar = True
while continuar:
    formaTitulo('MENU PRINCIPAL', 50, tab=True)
    print('-'*50)
    try:
        op = int(input('Sua opção: '))
    except Exception as erro:
        print(f'Erro! O erro encontrado foi por causa do {erro.__class__}')
        print('Você digitou uma opção invalida! Escolha novamente...')
    else:
        try:
            continuar = escolha(op)
        except ValueError:
            print('Você digitou uma opção invalida! Escolha novamente...')

        except Exception as erro:
            print(f'Erro {erro.__class__}')
            print('Você digitou uma opção invalida! Escolha novamente...')

