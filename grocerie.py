cart = {}

while True:
    try:
        item = input("").upper()
    
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    except EOFError:
            for item,qtd in cart.items():
                print(f"{qtd} {item}")
            break
        
    
    

