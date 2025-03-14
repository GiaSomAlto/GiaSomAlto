def somar(a, b):
    return a + b
    
def subtrair(a, b):
    return a - b
    
def multiplicar(a, b):
    return a * b
    
def dividir(a, b):
    if b == 0:
        return 'erro! divisão por 0'
    return a / b
    
def calculadora():
    print('escolha uma operação:')
    print('1 - somar')
    print('2 - subtrair')
    print('3 - multiplicar')
    print('4 - dividir')
    
    escolha = input('digite o numero da operação (1/2/3/4): ')
 
    num1 = float(input('digite o primeiro número: '))
    num2 = float(input('digite o segundo número: '))
    
    if escolha == '1':
        print(f'resultado: {somar(num1, num2)}')
    elif escolha == '2':
        print(f'resultado: {subtrair(num1, num2)}')
    elif escolha == '3':
        print(f'resultado: {multiplicar(num1, num2)}')
    elif escolha == '4':
        print(f'resultado: {dividir(num1, num2)}')
    else:
        print('operação inválida!')
calculadora()
