altura = float(input(' Digite sua altura '))
sexo = input('Digite seu sexo (M) ou (F) ')
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7
if sexo == "M":
    print(' Sexo masculino ', peso_ideal_h)
else:
    print(' Feminino ', peso_ideal_m)
