nota1 = float(input(' Digite a primeira nota '))
nota2 = float(input(' Digite outro número '))
nota_valida = nota1 >= 0.0 and nota1 <= 10.0
nota_valida = nota2 >= 0.0 and nota2 <= 10.0
media = (nota1 + nota2) / 2
if nota_valida:
    print(media)
else:
    print(' Nota invalida ')
