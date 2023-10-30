salas = [
    ['Lucas', 'Anna Clara'],
    ['Luciene', 'Vicente'],
    ['Helena', 'Samuel', (10, 20, 30)],
]

print(salas[0][1])
print(salas[2][2][2])

for sala in salas:
    for aluno in sala:
        print(aluno)
