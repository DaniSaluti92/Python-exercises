l=int(input("digite a largura:"))
h=int(input("digite a altura:"))

b=1
while (b<=h):
    if (b>1) and (b<h):
        a=1
        while (a<=l):
            if (a==1) or (a==l):
                print("#", end='')
            else:
                print(" ", end='')
            a=a+1
    else:
        a=1
        while (a<=l):
            print("#", end='')
            a=a+1
            
    print(end="\n")
    b=b+1
