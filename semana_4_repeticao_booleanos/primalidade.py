n=int(input("Digite um número inteiro:"))
i=n

while i>1:
	d=n/i
	r=n%i
	if (r==0):
		soma=n+d
	i=i-1

if soma==(n+1):
	print("primo")
else:
	print("não primo")
