def whileBreaker():
        
        continuar = input('Gostaria de adicionar outra pessoa? S/N  ').strip().lower()

        while continuar not in 'sn':
            print('Opção inválida!')
            continuar = input('Gostaria de adicionar outra pessoa? S/N  ').strip().lower()

        if continuar in 'n':
            return False
        elif continuar in 's':
             return True


