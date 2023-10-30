frase = ' Olha só que, coisa interessante '
lista_palavras = frase.split(',')
print(lista_palavras)
lista_frases_fixed = []

for i, frase in enumerate(lista_palavras):
    lista_frases_fixed.append(lista_palavras[i].strip())

frases_unidas = '-'.join(lista_frases_fixed)

print(lista_palavras)
print(lista_frases_fixed)
print(frases_unidas)