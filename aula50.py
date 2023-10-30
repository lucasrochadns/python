"""Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Lucas'
iteratador = iter(texto)
for letra in texto:
    try:
        print(iteratador.__next__())
    except StopIteration:
        break

print(' ------ ')
iteratador2 = iter(texto)
while True:
    try:
        letra = next(iteratador2)
        print(letra)
    except StopIteration:
        break
print('----------')
for letra in texto:
    print(letra)