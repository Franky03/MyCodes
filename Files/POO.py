from datetime import datetime
from random import *
from prettytable import PrettyTable

class Pessoa:
    ano_atual= int(datetime.strftime(datetime.now(), "%Y"))

    #Métodos de instancia
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome= nome
        self.idade= idade
        self.comendo= comendo
        self.falando= falando
        variavel= 'Valor'
    # def outro_metodo(self):
    #     print(self.nome)
    #     print(variavel)
    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return
        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando= True
    
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        print(f"{self.nome} parou de falar.")
        self.falando= False
    
    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return        
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo= True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo= False
    def ano_nascimento(self):
        print(self.ano_atual- self.idade)
    
    #Método de classe
    @classmethod #não é referente à instancia em si, mas à classe
    def por_nascimento(cls, nome, ano_nascimento):
        idade= cls.ano_atual- ano_nascimento
        return cls(nome, idade)
    
    #Método estático
    @staticmethod
    def gerar_id(): #não recebe parametros(self, cls), pode receber mas não é obrigatório
        rand= randint(10000, 199999)
        return rand



# p1= Pessoa('Luiz', 29)
# p2= Pessoa('João', 15)
# p1.falar("Marvel")
# p2.falar("DC")
# p2.parar_falar()
# p2.comer('amendoim')
# p1.parar_falar()
# p1.falar('Pokemon')
# print(Pessoa.ano_atual)
# print(p1.ano_nascimento())
# print(p2.ano_nascimento())
# p1= Pessoa.por_nascimento('Luiz', 1987)
# p1= Pessoa('Luiz', 32)
# print(p1)
# print(p1.nome, p1.idade)
# p1.ano_nascimento()
# print(p1.gerar_id())
# print(Pessoa.gerar_id())

class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco= preco
    
    def desconto(self, percentual):
        self.preco= self.preco- (self.preco * (percentual/100))

    #Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor= float(valor.replace('R$', ''))
        self._preco= valor

    #Getter
    @property
    def nome(self):
        return self._nome
    #Setter
    @nome.setter
    def nome(self, string):
        self._nome= string.replace('A', '@')


p1= Produto('Camisa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2= Produto('CANECA', 'R$15')
# p2.desconto(10)
print(p2.preco)
print(p2.nome)

#Atributos de classe
class A:
    vc=123
    def __init__(self):
        pass
        # self.vc= 321

# a1= A()
# a2= A()
# A.vc= 'Alterado'
# a1.vc=321
# print(a1.__dict__)
# print(a2.__dict__)
# print(a1.vc)
# print(a2.vc)
# print(A.vc)

#Encapsulamento
class BaseDeDado:
    def __init__(self):
        self.__dados= {}

    def lista_clientes(self):
        table= PrettyTable()
        table.field_names= ['ID', 'Clientes']
        for k, v in self.__dados['clientes'].items():
            table.add_row([k, v])
        print(table)
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes']= {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def remover_cliente(self, id):
        del self.__dados['clientes'][id]

# bd= BaseDeDado()
# bd.inserir_cliente(1, 'Otávio')
# bd.inserir_cliente(2, 'Rose')
# bd.inserir_cliente(3, 'Marcelo')
# bd.inserir_cliente(4, 'Julio')
# bd.remover_cliente(3)
# bd.lista_clientes()

#Associação de classes
class Escritor:
    def __init__(self, nome):
        self.__nome= nome
        self.__ferramenta= None

    @property
    def nome(self):
        return self.__nome
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta= ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca= marca
    
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo...")
    
class MaquinaDeEscrever:
    def escrever(self):
        print("Máquina está escrevendo...") 


escritor= Escritor('Otávio')
caneta= Caneta('Bic')
maquina= MaquinaDeEscrever()

escritor.ferramenta= caneta
escritor.ferramenta.escrever()
print(escritor.ferramenta.marca) 
caneta.escrever()

#Agregação

class Carrinho:
    def __init__(self):
        self.produtos=[]

    def inserir(self, produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        table= PrettyTable()
        table.field_names= ['Produtos', 'Preço']
        for p in self.produtos:
            table.add_row([p.nome, p.valor])
        total=0
        for produto in self.produtos:
            total+=produto.valor
        table.add_row(['TOTAL' ,total])
        print(table)
       
class Produto:
    def __init__(self, nome, valor):
        self.nome= nome
        self.valor= valor

# carrinho= Carrinho()
# p1= Produto('Playstation', 1549)
# p2= Produto('Iphone', 6890)
# p3= Produto('Camiseta', 56)
# p4= Produto('Cabo USB', 35)
# carrinho.inserir(p2)
# carrinho.inserir(p1)
# carrinho.inserir(p3)
# carrinho.inserir(p4)
# carrinho.lista_produto()

#Composição

class Cliente:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade
        self.enderecos= []
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #Usou a classe endereço para compor um cliente na classe Cliente

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado) 
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')



class Endereco:
    def __init__(self, cidade, estado):
        self.cidade= cidade
        self.estado= estado
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')


# c1= Cliente('Luiz', 32)
# c1.insere_endereco('Belo Horizonte', 'MG')
# print(c1.nome)
# c1.lista_enderecos()
# # del c1
# print()

# c2= Cliente('Maria', 55)
# c2.insere_endereco('Salvador', 'BA')
# c2.insere_endereco('Rio de Janeiro', 'RJ')
# print(c2.nome)
# c2.lista_enderecos()
# # del c2
# print()

# c3= Cliente('João', 19)
# c3.insere_endereco('São Paulo', 'SP')
# print(c3.nome)
# c3.lista_enderecos()
# # del c3
# print('___________________')

#VEJA A DIFERENÇA DEPOIS DESSA LINHA COM O DEL C1, DEL C2 E DEL C3
#Quando a classe cliente é criada e cria uma classe endereço, assim que ela for apagada, a classe endereço também será apagada da memória
#Quando uma morrer a outra também morre

#Herança simples
class Pessoa: #SuperClasses
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade=idade
        self.nomeclasse= self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')
#SubClasses
class Client(Pessoa): #Um cliente é uma pessoa, ele herda o que tem dentro de pessoa
    
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')

c1= Client('Luiz', 45)
c2= Aluno('Jão', 15)
print(c1.nome)
c1.falar()
c1.comprar()
#c1.estudar() dá errado pq não existe no c1
print(c2.nome)
c2.falar()
c2.estudar()

p1= Pessoa('Maria', 50)
p1.falar()

class Animal:
    def __init__(self):
        self.num_eyes=2
    
    def breathe(self):
        print('Inhale, Exhale')

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing this under water")

nemo= Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
