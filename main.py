from conta import Conta
from conta import Cliente

import os
pessoa = [['marilda', 1234, 45], ['lucas', 1234, 56]]

n = input('nome:')
c = int(input('cpf:'))
i = int(input('idade:'))
n =  Conta(n, c, i)
cpfs = [row[1] for row in pessoa]
for num in cpfs:
    if num == n.cpf:
        print('ja existe esse cpf')
    else:
        pass
pessoa.append([n.nome, n.cpf, n.idade])
os.system('cls' if os.name == 'nt' else 'clear')
sal = 0
dep = 0
sac = 0
while True:
    print('entrando...')
    print('====================================')
    print('                                    ')
    print('              BANCO                 ')
    print('       conta:', n.nome,'           ')
    print('====================================')
    
    nome_cliente  = Cliente(sac, dep, sal)
    print('= 1. Despositar')
    print('= 2. Sacar')
    print('= 3. Consultar saldo')
    resp = int(input('= O que deseja fazer: '))
    #adicionar valores ao [saldo]
    if resp == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_cliente.depositar = int(input('quanto deseja despositar R$ :',))
        sac += nome_cliente.depositar 
        print('seu saldo agora e:', sac, 'R$')
    #retirar valores do [saldo]
    elif resp == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        nome_cliente.sacar = float(input('quanto deseja sacar R$ :'))
        nome_cliente.saldo -  nome_cliente.sacar
    #consultar valor do [saldo]
    elif resp ==  3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('seu saldo e :', nome_cliente.saldo)
    else:
        print('comando indisponivel')
