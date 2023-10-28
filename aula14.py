a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

#parametro nomeado variavel na string b={nome2} no method format recebe o valor de b
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
print(string)

#indices lembrando a ordem do method
nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

formato = f'{nome} tem {idade:.2f} anos'
print(formato)

numero_1 = 10
numero_2 = 20
resultado = numero_1 * numero_2
print(resultado)
