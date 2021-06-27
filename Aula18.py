teste = list()
teste.append('gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #colocando lista teste dentro de lista galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)