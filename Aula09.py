frase = '   Curso em Vídeo Python'
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[::2])
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android')) #string é imutavel, logo isso não replace ela pra sempre somente nesse momento
print(frase.find('Vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0][3])

#para escrever um texto inteiro

print("""amanda
blablablabla
lalalalallala""")



