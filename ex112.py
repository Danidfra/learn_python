from func.dado import leiaDinheiro;
from func.moeda import resumo;

p = leiaDinheiro('Digite o preço: R$')
pa = float(input('Digite a porcentagem que será acrescentada: '))
pr = float(input('Digite a porcentagem que será decrescida: '))

resumo(p, pa, pr)