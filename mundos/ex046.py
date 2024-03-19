from time import sleep;

nmr_contagem = int(input('Em quanto tempo devo lançar os fogos de artifício? '))

for i in range(nmr_contagem, -1, -1):
    print(i)
    sleep(1)

print('Fogos lançados!')
sleep(4)
print('Linda explosão de fogos rsrs...')