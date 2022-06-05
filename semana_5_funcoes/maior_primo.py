def maior_primo(x):
    n=x
    
    while  n>=1:
        i=n
        soma = 0
        while i>1:
            d=n/i
            r=n%i
            if (r==0):
                soma=n+d
            i=i-1
        if soma==(n+1) or n==1:
           return(n)
           n=0
        if (n!=0):
            n=n-1
    
