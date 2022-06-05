n=int(input("Digite um número inteiro:"))
i=10
b=0.6
c=0.5
a=1
while b!=c and a!=0:
	c=b
	a=n//10
	b=n%10
	n=a
	if (b==c):
		print("sim")
if (a==0 and b!=c):
	print("não")
