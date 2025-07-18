dinheiro = False
senha = True

if dinheiro == True and senha == True:
    print('Sacar')

elif dinheiro == True and senha == False:
    print('Senha inválida')
    
elif dinheiro == False and senha == True:
    print('Saldo insuficiente')

elif dinheiro == False and senha == False:
    print('Dados incorretos')