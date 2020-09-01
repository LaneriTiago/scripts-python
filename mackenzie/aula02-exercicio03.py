#Faça um algoritmo para calcular a média aritmética
#entre duas notas de um aluno e mostrar sua situação,
#que pode ser aprovado ou reprovado

n1 = float (input('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
media = (n1 + n2)/2
if media < 7:
    print ('Média {}: reprovado' .format (media))
else:
    print ('Média {}: aprovado' .format (media))
    
