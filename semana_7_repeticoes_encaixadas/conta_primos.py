def primo(n):
    i=n
    soma = 0
    while i>1:
        d=n/i
        r=n%i
        if (r==0):
            soma=n+d
        i=i-1
    if soma==(n+1) or n==1:
        c=1
    else:
        c=0
    return (c)

def n_primos(x):
    d=2
    soma=0
    while(d<=x):
        c=primo(d)
        soma=soma+c
        d=d+1
    return(soma)
