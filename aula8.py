nome = 'Lucas'
sobrenome = 'Rocha dos Santos'
idade = 28
ano_nascimento = 2023 - idade
maior_de_idade = idade >= 18
altura_metros = 1.82

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

print(type(nome), type(sobrenome), type(ano_nascimento), type(maior_de_idade), type(altura_metros), sep=" : ")