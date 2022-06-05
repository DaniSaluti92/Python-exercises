lista=[]
a=0.5
while(a!=0):
    a=int(input("Digite um número:"))
    lista.append(a)
del lista[-1]

l=len(lista)
b=1

while (b<=l):
    print (lista[-b])
    b=b+1
    
