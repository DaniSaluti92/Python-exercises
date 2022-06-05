def remove_repetidos(lista):
    l=len(lista)
    a=0
    while (a<l):
        b=0
        while(b<l):
            if (a!=b) and (lista[a]==lista[b]):
                del lista[b]
                l=len(lista)
            b=b+1
        a=a+1

    return sorted(lista)
