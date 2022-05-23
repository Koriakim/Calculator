# Trabalhando com IF, ELSE E ELIF

print('Seja bem vindo... ')

operador = input('Insira a operação +, -, /, *: ')

number_1 = int(input('Insira o primeiro numero: '))
number_2 = int(input('Insira o segundo numero: '))

if operador == '+':
    print(f'{number_1} + {number_2} =', float(number_1 + number_2))
elif operador == '-':
    print(f'{number_1} - {number_2} =', float(number_1 - number_2))
elif operador == '/':
    print(f'{number_1} / {number_2} =', float(number_1 / number_2))
elif operador == '*':
    print(f'{number_1} * {number_2} =', float(number_1 * number_2))
else:
    'Reinicialize o programa e digite o operador correspondente a lista...'

