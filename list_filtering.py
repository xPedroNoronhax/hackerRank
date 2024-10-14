#remova as strungs da lista, e retorne uma lista sem strings
def filter_list(l):
    answear = []
    for i in l:
        if type(i) != str:
           answear.append(i)
    return answear

print(filter_list([1, 2, "aasf", "1", "123", 123]))