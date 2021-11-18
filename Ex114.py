#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except: #ou except urllib.error.URLError:
    print('Deu erro')
else:
    print('tudo ok')
    print(site.read())