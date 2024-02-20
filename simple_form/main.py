def my_function_test():
    wrongQ = input("Quantas informações gostaria de trocar? ")

    if wrongQ == "1":

        troca = input("Qual informação gostaria de trocar? ")

        if troca == "nome":
            nome = input("Qual é o nome correto? ")
        elif troca == "idade":
            idade = input("Qual é a idade correta? ")
        elif troca == "peso":
            peso = input("Qual é o peso correto? ")

        print(f"Atualizando minhas informações você se chama {nome} tem {idade} anos, e esta pesando atualmente {peso} kgs.")
        valid = input("Agora as informações estão corretas? s/n ")

        if valid == "s":
            print(f"Obrigado {nome}! Tenha um bom dia!")
        else:
            my_function_test()

    elif wrongQ == "2":
        
        wrong1 = input("Qual a primeira informação que gostaria de trocar? nome/idade/peso ")
        if wrong1 == "nome":
            nome = input("Qual é o nome correto? ")
            wrong2 = input("Qual a segunda informação que gostaria de trocar? idade/peso ") 
        elif wrong1 == "idade":
            idade = input("Qual é a idade correta? ")
            wrong2 = input("Qual a segunda informação que gostaria de trocar? nome/peso ") 
        elif wrong1 == "peso":
            peso = input("Qual é o peso correto? ")
            wrong2 = input("Qual a segunda informação que gostaria de trocar? nome/idade ")

        if wrong2 == "nome":
            nome = input("Qual é o nome correto? ")
        elif wrong2 == "idade":
            idade = input("Qual é a idade correta? ")
        elif wrong2 == "peso":
            peso = input("Qual é o peso correto? ")

        print(f"Atualizando minhas informações você se chama {nome} tem {idade} anos, e esta pesando atualmente {peso} kgs.")
        valid = input("Agora as informações estão corretas? s/n ")

        if valid == "s":
            print(f"Obrigado {nome}! Tenha um bom dia!")
        else:
            my_function_test()

    elif wrongQ == "3":

        nome = input("Qual é o nome correto? ")
        idade = input("Qual é a idade correta? ")
        peso = input("Qual é o peso correto? ")
        
        print(f"Atualizando minhas informações você se chama {nome} tem {idade} anos, e esta pesando atualmente {peso} kgs.")
        valid = input("Agora as informações estão corretas? s/n ")

        if valid == "s":
            print(f"Obrigado {nome}! Tenha um bom dia!")
        else:
            my_function_test()


nome = input("Qual é seu nome? ")
idade = input("Qual é sua idade? ")
peso = input("Qual é seu peso? ")

print(f"Ola {nome}, pelo que me foi informado você tem {idade} anos, e esta pesando atualmente {peso} kgs.")
condi = input("As informações anteriores estão corretas? s/n ")

if condi == "S":
    print(f"Obrigado {nome}! Tenha um bom dia!")
else:
    
    my_function_test()
        # continueQ = input("Conseguiu corrigir todas as informações que estavam erradas? s/n ")

        # if continueQ == "n":
            
    
    # nmr = float(input("Digite um numero... "))

    # print(type(nmr))


