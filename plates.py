def main():
    # Pede ao usuário para inserir uma placa de vaidade
    plate = input("Plate: ")
    
    # Verifica se a placa é válida e imprime o resultado
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Verifica se a placa tem entre 2 e 6 caracteres
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Verifica se os dois primeiros caracteres são letras
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Verifica se há números no final e se não há números no meio
    letters = ""
    numbers = ""
    for char in s:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char
    
    # Se houver números, eles devem estar no final
    if len(numbers) > 0 and s[len(letters):] != numbers:
        return False
    
    # Se a placa tem números, verifica se o primeiro número não é '0'
    if len(numbers) > 0 and numbers[0] == '0':
        return False

    return True  # Se todas as verificações passarem, a placa é válida

# Executa o programa
main()
