#Um banco concederá um crédito especial a seus clientes de acordo com o saldo médio no último ano. Faça
#um pseudocódigo que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela
#a seguir. Mostre o saldo médio e o valor do crédito.

saldo_medio = float (input('Digite o saldo médio: '))

if saldo_medio > 400:
    credito = saldo_medio * 0.3

elif saldo_medio >= 300.01: 
    credito = saldo_medio * 0.25

elif saldo_medio >= 200.01:
    credito = saldo_medio * 0.2
    
else: 
    credito = saldo_medio * 0.1

print ('Saldo medio:  R$ ', saldo_medio) 
print ('Crédito:  R$ ', credito)

    
