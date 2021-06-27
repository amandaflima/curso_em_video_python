try:
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    r = a / b
#except Exception as erro:
 #   print(f'ERRO de {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados inseridos')
except ZeroDivisionError:
    print('Nao é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O erro foi {erro.__cause__}')
else:
    print(r)
finally:
    print('volte sempre')