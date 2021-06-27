'''nome = str(input('Qual é o seu nome? '))
if nome == 'Amanda':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {}'.format(m))

'''if m>=6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')'''

print('Sua média foi boa' if m >= 6 else 'Sua média foi ruim')