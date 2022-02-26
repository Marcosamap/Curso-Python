import math
num = int(input(' Digite um numero '))
if num > 0:
    num_log = math.log(num, 2)
    print('math.log(100.2)', num_log)
else:
    print(' Número invalido ')
