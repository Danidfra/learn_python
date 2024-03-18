from math import factorial, floor, ceil;
# import random;

def nmr_f(x):
    r = factorial(x)

    print(f"O resultado depor de fatorar o numero {x} é {r}.")

    q2 = input("Gostaria de fatorar outro número? s/n ")

    if q2 == "s":
        nmr = int(input("Qual o proximo número que devo fatorar?"))
        nmr_f(nmr)

    else: 
        print("Tchau tchau, ate a proxima!")


q1 = input("Gostaria de fatorar algum número? s/n ")

if q1 == "s":
    nmr = int(input("Digite o número que você quer fatorar: "))
    nmr_f(nmr)

else:
    print("Tchau tchau, ate a proxima!")


# nmrA = random.random() * 10

# print(nmrA)
# print(ceil(nmrA))
# print(floor(nmrA))