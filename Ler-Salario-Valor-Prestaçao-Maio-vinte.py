salario = float(input(' Digite seu salario '))
prestacao = float(input(' Digite o valor Prestação '))
porcetagem = salario * 20 / 100
if prestacao <= porcetagem:
    print(' Emprestimo consedido ')
else:
    print(' Emprestimo não consedido ')
