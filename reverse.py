def reverse_list(liste):
    m = []
    for i in liste:
        if isinstance(i,list):
            m.append(reverse_list(i))
        else:
            m.append(i)
    m.reverse()
    return m

l=[[1, 2], [3, 4], [5, 6, 7]]
print(reverse_list(l))