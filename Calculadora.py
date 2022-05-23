# Projeto final

def welcome():
    print('''
    Bem vindo a calculadora Python!!!
    ''')


def calculator():
    operator = input('''Insira a operação logica
     + Para Adição
     - Para Subtração
     / Para Divisão
     * Para Multiplicação 
     : ''')
    numero1 = int(input('Insira o primeiro numero: '))
    numero2 = int(input('Insira o segundo numero: '))

    if operator == '+':
        print(f'{numero1} + {numero2} =', numero1 + numero2)
    elif operator == '-':
        print(f'{numero1} - {numero2} =', numero1 - numero2)
    elif operator == '/':
        print(f'{numero1} / {numero2} =', numero1 / numero2)
    elif operator == '*':
        print(f'{numero1} * {numero2} =', numero1 * numero2)
    else:
        'Você não inseriu um operador logico correto, inicie o programa novamente...'
    # Importante para chamar a função again() assim que a função calculator() se encerre.
    again()


def again():
    calc_again = input('Deseja reutilizar a calculadora? (Y/N): ')
    # Se o usuário digitar 'Y' chamara a função 'calculator()' para reutilizar a calculadora
    if calc_again.upper() == 'Y':
        return calculator()
    # Caso o usuário digite 'N' código encerra e exibirá uma mensagem de despedida
    elif calc_again.upper() == 'N':
        print('Vejo você mais tarde...')
    else:
        again()


# Chamada da função calculator() + welcome()
welcome()
calculator()
