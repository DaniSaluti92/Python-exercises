import math

def é_hipotenusa(n):
    j=1
    while (j<n):
        i=1
        while(i<n):
            a=(i**2)+(j**2)
            hipotenusa=(math.sqrt(a))      
            i=i+1
            if (hipotenusa==n):
                return(hipotenusa)
                break   
        j=j+1

    
    
def soma_hipotenusas(n):
    soma=0
    a=1
    while(a<=n):
        h=str(é_hipotenusa(a))
        if (h!= "None"):
            i=float(h)
            soma=soma+i
        a=a+1
    return(soma)
