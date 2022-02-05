
print('Bem Vindo a calculadora')

print()

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input(' Digite o segundo numero: '))

con = input('Digite o tipo de conta que ira fazer (+,-,*,/,%): ')
    # Escolher a condição para o calculo


if con == '+':
    print('Sua Resposta é')
    print(round(num1 + num2,2))

elif con == '-':
    print('Sua Resposta é')
    print(round(num1 - num2,2))

elif con == '*':
    print('Sua Resposta é')
    print(round(num1 * num2,2))

elif con == '/':
    print('Sua Resposta é')
    print(round(num1/num2,2))

elif con == '%':
    print('Sua Resposta é')
    print(round(num1 % num2))

else:
    print('Resposta invalida')

    while con != '+' and con != '-' and con != '*' and con != '/' and con != '%':
        # Repetição caso a pessoa expecifique errado o tipo de conta

        con = input('Digite o tipo de conta que ira fazer (+,-,*,/,%): ')

        if con == '+':
            print('Sua Resposta é')
            print(round(num1 + num2, 2))

        elif con == '-':
            print('Sua Resposta é')
            print(round(num1 - num2, 2))

        elif con == '*':
            print('Sua Resposta é')
            print(round(num1 * num2, 2))

        elif con == '/':
            print('Sua Resposta é')
            print(round(num1 / num2, 2))

        elif con == '%':
            print('Sua Resposta é')
            print(round(num1 % num2))

