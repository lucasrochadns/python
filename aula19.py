primeiro_valor = input('Insira um valor: ')
segundo_valor = input('Insira outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor} é maior que {primeiro_valor}')
else:
    print(f'{primeiro_valor} são iguais {segundo_valor}')
