
# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
elif senha != '123456':
    print('Senha incorreta ')
else:
    print("Login Sucess Full")

print(not True)  # False
print(not False)  # True