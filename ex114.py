import urllib
from urllib.request import urlopen


with urlopen("https://www.pudim.com.br/") as response:
    try:
        site = response
    except:
        print('Erro')
    else:
        print('Deu certo')
        