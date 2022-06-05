def maximo(a,b,c):
    if ((a>=b) and (a>c)) or ((a>b) and (a>=c))or ((a==b) and (b==c)):
        return a
    if ((b>=a) and (b>c)) or ((b>a) and (b>=c)):
        return b
    if ((c>=a) and (c>b)) or ((c>a) and (c>=b)):
        return c
    
