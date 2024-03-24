# def formaTitulo(tex, tam, item='pessoa', tab=False):
#     print('-'*tam)
#     print(tex.center(tam))
#     print('-'*tam)

#     if tab:
#         print(f'1 - Ver {item}s cadastradas')
#         print(f'2 - Cadastrar {item}')
#         print('0 - Sair do Sistema')

class Tabela():

    def __init__(self, tam, item):
        self.tam = tam
        self.item = item

        
    def montar(self,title,cab=False, text='',tab=True):    
        print('-'*self.tam)             
        print((title.upper()).center(self.tam))
        print('-'*self.tam)
        if cab:
            print(f'{text}')
        if tab:
            for c,i in enumerate(self.item, start=1):
                    print(f'{c} - {i}')
            print()
            print('-'*self.tam)