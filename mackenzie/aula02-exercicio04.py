#Escreva um algoritmo para calcular o novo salário de um funcionário.
#Sabe-se que os funcionários que recebem atualmente salário de
#até R$ 500 terão aumento de 20%; os demais terão aumento de 10%:

salario = float (input('Digite o salário: '))
if salario <= 500:
    print ('salario atualizado (+20%): R$ ', salario*0.2+salario)
else:
    print ('salario atualizado (+10%): R$ ', salario*0.1+salario)
    
