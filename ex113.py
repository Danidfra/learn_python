from mundos.ex104 import leiaInt;

while True:
    try:
        i = int(input('Digite um Inteiro: '))
    except ValueError:
        print('ERRO! O valor informado não é um número inteiro.')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse número.')
    except Exception as erro:
        print(f'Erro ao receber o input. O tipo de erro foi {erro.__class__}')
    else:
        break

while True:
    try:
        r = float(input('Digite um Real: '))
    except ValueError:
        print('ERRO! O valor informado não é um número real.')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse número.')
    except Exception as erro:
        print(f'ERRO! O erro encontrado foi {erro.__class__}!')
    else:
        break

leiaInt(i, r)