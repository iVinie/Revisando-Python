num1 = int(input('Digite o primeiro número:\n'))
num2 = int(input('Digite o segundo número:\n'))

#Soma
sum = num1 + num2
#Subtração
sub = num1 - num2
#Divisão
div = num1/num2
#Multiplicação
mult = num1*num2
#Resto da divisão
rdd = num1%num2
#exponencial
exp = num1**num2

print (f'Soma: {sum}\nSubtração: {sub}\nDivisão: {div}\nMultiplicação: {mult}\nResto da divisão: {rdd}\nExponencial: {exp}')

#Operadores de compraração:
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

#Atribuição

num1 += 1 #Isto é num1 = num1 + 1, mesmo vale para subtração, divisão...
