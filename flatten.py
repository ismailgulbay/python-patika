def flatten(liste):
    m = []

    if isinstance(liste,list):
        for i in liste:
            m.extend(flatten(i))
    else:
        m.append(liste)
    return m

a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b = [[1, 2], [3, 4], [5, 6, 7]]
print(flatten(a))

