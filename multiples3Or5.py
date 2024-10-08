def solution(number):
    multiples = []
    i = 1
    
    while i < number -1 :
        i+=1
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    
    result = sum(multiples)
    print(multiples)

    if result > 0:
        return result
    else:
        return 0



print(solution(6))



"""
vc recebe determinado numero. 
precisa contar de 0 até ele, e ver nesse caminho quais numeros são multiplos de 3 ou 5.
se o numero for multiplo coloque ele em um array
depois de percorrer todos, some todos os numeros do array.
retorne essa soma.
se number < 0, retorne 0
"""