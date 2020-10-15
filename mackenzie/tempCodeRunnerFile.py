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