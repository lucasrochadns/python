# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

print(int('100') * 10)
print('Lucas Rocha ' + str('28'))
idade = 28
maiorQue = idade > 18
print('E de maior? ', maiorQue, sep=":") 