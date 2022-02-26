num = int(input(' Digite um número inteiro '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if num > 0:
    soma = u + d + c + m
    print(soma)
else:
    print(' Número invalido ')
