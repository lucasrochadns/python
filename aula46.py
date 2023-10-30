#While else que isso homen ?

valor_teste = 'string qualquer'
contador = 0
while contador < len(valor_teste):
    letra = valor_teste[contador]
    print(letra)
    contador += 1
else:
    print('O else foi executado')