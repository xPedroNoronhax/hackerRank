import inflect
p = inflect.engine()

salve = []
person = input("Name: ")
try:
    while True:
        while person != "":
            salve.append(person)
            person = input("Name: ")
        salve = tuple(salve)
        adieu = p.join(salve)
        print(f"Adieu, adieu, to ", adieu)
except EOFError:
    pass