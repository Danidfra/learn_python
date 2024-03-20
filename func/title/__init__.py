# def formaTitulo(tex, tam, item='pessoa', tab=False):
#     print('-'*tam)
#     print(tex.center(tam))
#     print('-'*tam)

#     if tab:
#         print(f'1 - Ver {item}s cadastradas')
#         print(f'2 - Cadastrar {item}')
#         print('0 - Sair do Sistema')

class Tabela():

    def __init__(self, text, tam, item):
        self.text = text
        self.tam = tam
        self.item = item

        
    def montarTabela(self):    
        print('-'*self.tam)
        print((self.text).center(self.tam))
        print('-'*self.tam)

        for c,i in enumerate(self.item, start=1):
                print(f'{c} - {i}.')

        print('-'*self.tam)