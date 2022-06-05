def soma_elementos(lista):
    l=len(lista)
    soma=0
    a=1
    while(a<=l):
        soma=soma+(lista[-a])
        a=a+1
    return soma
    
