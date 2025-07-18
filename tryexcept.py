#TRYEXCEPT

try:
    numero = int (input('Digite um número: '))

    #print('Deu bom! ')
    if( numero % 2 == 0):
        print('Par')

    elif(numero % 2 != 0):
        print('Ímpar')
    
except:
    print('Número inválido')
    