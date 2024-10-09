"""
valor_da_coca = 50
imprima valor da coca: valor_da_coca
pagamento = x
    se pagamento == 5 ou pagamento == 10 ou pagamento == 25:
        valor_da_coca = valor_da_coca - pagamento
    enquanto valor_da_coca > 0:
        imprima valor da coca: valor_da_coca
        se pagamento == 5 ou pagamento == 10 ou pagamento == 25:
        valor_da_coca = valor_da_coca - pagamento
    
    retorne valor_da_coca
    


"""
coke_value = 50
print(f"Amount Due: {coke_value}")
payment = int(input("Insert Coin: "))
if payment == 5 or payment == 10 or payment == 25:
    coke_value = coke_value - payment
while coke_value > 0:
    print(f"Amount Due: {coke_value}")
    payment = int(input("Insert Coin: "))
    if payment == 5 or payment == 10 or payment == 25:
        coke_value = coke_value - payment

print(f"Change Owed: {abs(coke_value)}")
        
