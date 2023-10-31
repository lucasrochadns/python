import decimal

x = input('Informe o valor 1 ')
y = input('Informe o valor 2 ')

def soma(x, y):
    print(f'Soma e {x + y:.2f}')

soma(decimal.Decimal(x), decimal.Decimal(y))