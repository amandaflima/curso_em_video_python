'''lanche = ('Hamburguer', 'Suco', 'Pizza')

print(sorted(lanche)) #coloca a tupla em ordem

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #te da a posição

for cont in range(0, len(lanche)):
    print(lanche[cont])  #te da a posiçao

#for comida in lanche:
#    print(f'Eu vou comer {comida}')
print('Comi muito')'''

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #nao soma, apenas junta
print(c)
print(c.count(5)) # mostra quantas vezes o numero 5 aparece
print(c.index(8)) #mostra a posição do 8
print(c.index(2, 1)) #ignora o primeiro 2 e mostra a posição do proximo 2'''

pessoa = ('Gustavo', 39, "M")
del(pessoa) #apaga o elemento pessoa, não pode apagar um elemento da tupla, apenas a tupla inteiro
print(pessoa)