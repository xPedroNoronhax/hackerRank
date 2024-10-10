"""
medidor de combustivel
mostrar para o usuario a porcentagem que possui no tanque.
1/4 = 25%
1/2 = 50%
3/4 = 75%
divisão maior ou igual 99% = F
divisão menor ou igual a 1% = E

programa vai perguntar a fração:
fração: x/y
separe as strings,oque tiver antes de "/" é int(x) e depois é int(y)


"""

#converte a string em duas variaveis x e y
def convert(string):
    x, y = string.split("/")
    x = int(x)
    y = int(y)
# utilizasse do raise para apontar erros de zerodivision e valueError
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return round((x/y) * 100)

#funcao que retorna uma resposta baseada na porcentagem oferecida
def gauge(percent):
    if percent > 99:
        return "F"
    elif percent <= 1:
        return "E"
    else: 
        return f"{int(percent)}%"

while True:
    try:
        fraction = input("Fraction: ")
        percent = convert(fraction)
        print(gauge(percent))
        break
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
