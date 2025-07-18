#Modulo

"""
1 igual se refere a uma atribuição
2 iguais referem-se a uma comparação
"""

print(12 % 4 == 0)
print("___")

x = 10

y = 15

print( x == y )
print("---")

n = int (input('Digite um valor numérico -->'))

if(n %2 == 0):
    #print(f'0 {n} digitado é par')
    print('O número ->', n ,' digitado é par')
    print("---")

else:
    print('O número ->', n ,'digitado é impar')