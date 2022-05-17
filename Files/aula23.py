#Tratamento de erro
try: #Tente
    a= int(input('A:'))
    b= int(input('B:'))
    divi= a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário decidiu não informar os dados.')
except Exception as erro:  
    print(f'O erro encontrado foi : {erro.__class__}')
else:
    print(f'A divisão de {a} com {b} é {divi:.1f}')
finally:
    print('Volte sempre!!')
