def soma(n1=0, n2=0):
    return n1+n2
def multiplicar(n1=0, n2=0):
    return n1*n2
def dividir(n1, n2):
    return n1/n2
def subtrair(n1, n2):
    return n1-n2
def potencia(n1, n2):
    return n1 ** n2
def raiz(n1, n2):
    return n1 ** (1/n2)


print("--"*10)
print(f"{'CALCULADORA':^20}")
print("--"*10)
print(f"{'[+]Somar':<10}\n{'[-]Subtrair':<10}\n{'[*]Multiplicar':<10}\n{'[/]Dividir':<10}\n{'[P]Potencia':<10}\n{'[R]Raiz':<10}")
operation=['+', '-', '*', 'P', '/', 'R', 'r', 'p']
resp=''
while True:
    if resp=='y':
        num1= result
    else:
        num1=float(input("Primeiro número: "))
    while True:
        opc= str(input("Qual operação?: ")).strip().upper()
        if opc in operation:
            break
        else:
            print("ERROR")
    if opc=='P':
        num2=int(input("Digite o expoente: "))
    elif opc=='R':
        num2= int(input("Digite o índice: "))
    else:
        num2= float(input("Segundo número: "))
    if opc=='+':
        result= soma(num1,num2)
    elif opc=='-':
        result= subtrair(num1, num2)
    elif opc=='*':
        result= multiplicar(num1, num2)
    elif opc=='/':
        result= dividir(num1, num2)
    elif opc=='P':
        result= potencia(num1, num2)
        opc= '**'
    elif opc=='R':
        result= raiz(num1, num2)
        opc='*/'
    print(f"{num1} {opc} {num2}= {result}")
    while True:
        resp= str(input(f"Digite 'y' para continuar calculando com {result}, digite 'n' para um novo calculo ou digite 's' para sair: ")).lower().strip()
        if resp=='y' or resp=='n' or resp=='s':
            break
        else:
            print("ERROR")
    if resp=='s':
        break