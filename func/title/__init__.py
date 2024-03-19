def formaTitulo(tex, tam, tab=False):
    print('-'*tam)
    print(tex.center(tam))
    print('-'*tam)

    if tab:
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova Pessoa')
        print('0 - Sair do Sistema')
