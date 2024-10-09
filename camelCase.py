def camelCase(string):
##string to list
    string_list = list(string.strip().replace(" ",""))
    
    snake_case_string = ""
    for char in string_list:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    return snake_case_string

   

    


    






"""
voce vai receber uma string, pode ser com camelCase ou não.
se não for camelCase, retorne a string;
se for, mude ela para snake_Case
"""