nomes = ['Lucas', 'Rocha', 'Dos', 'Santos']
nome1, nome2, nome3, nome4 = nomes
print(f'Valor-1 {nome1} Valor-2 {nome2} Valor-3 {nome3} Valor4 {nome4}')

nome5, *resto = nomes
print(resto)
print(nome5)
print('---------')
_, nome6, *resto2 = nomes
print(nome6)
print(resto2)
