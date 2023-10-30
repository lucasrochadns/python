import decimal

numero_1 = 0.9
numero_2 = 0.7
numero_3 = decimal.Decimal('0.97')
numero_4 = decimal.Decimal('0.6')

print(round(numero_1 + numero_2, 2))
print(f'{numero_2 + numero_1:.2f}')
print(numero_3 + numero_4)