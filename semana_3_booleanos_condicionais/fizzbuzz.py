a=int(input("Digite um número inteiro"))
b=a/3
c=str(b)[-1]
d=int(c)

e=a/5
f=str(e)[-1]
g=int(f)


if(d==0 and g==0):
	print("FizzBuzz")
else:
	print(a)
