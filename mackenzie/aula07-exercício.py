# 2) Leia um conjunto de números inteiros, encerrando 
# a entrada de dados quando o usuário digitar 0 (zero). 
# Calcule e mostre a quantidade de números digitados e a soma desses números.
n = ''
soma = 0
qtd = 0
while n != 0:
    n = int (input('informe o número: '))
    soma += n
    qtd += 1

print (qtd-1)
print (soma)
