# remover os valores que estao presentes na lista b da lista a
# array_diff([1,2],[1]) == [2]
"""
percorra lista a de i até o final
    percorra lista b de i até o final
        se b[i] != a[i]
            nova_lista.append(a[i])
"""
def array_diff(a,b):
    new_list = []
    for i in a:
        if i not in b:
            new_list.append(i)
    print(new_list)


array_diff([1,2,2,2,3],[2])
