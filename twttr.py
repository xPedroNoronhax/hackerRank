"""
voce recebe uma string, precisa verificar se nela há vogais e retirar elas, retornando uma string sem vogal.
vogais = ['A','a','E','e','I','i','O','o','U','u']
string = x
stringSemVogal = ''
    para char em string:
        se char nao estiver em vogais:
            stringSemVogal += char
imprima(stringSemVogal)

    
       
"""

vogels = ['A','a','E','e','I','i','O','o','U','u'];
string = input('Input: ')
no_vogels_string = ''
for char in string:
    if char not in vogels:
        no_vogels_string += char
print(no_vogels_string)
