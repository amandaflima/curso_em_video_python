'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
num.remove(2)
del num[2]
print(num)
print(len(num))'''

'''valores = [] #ou valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor')))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')'''

a = [2, 3, 4, 7]
b = a[:] #cria uma copia de A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')