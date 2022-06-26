pessoas=[]
dados=[]
peso=[]
numero=0
while True:
    dados.append(input("Digite um nome: "))
    dados.append(int(input("Digite o peso dessa pessoa:")))
    pessoas.append(dados[:])
    print(pessoas[numero][1])
    numero+=1
    