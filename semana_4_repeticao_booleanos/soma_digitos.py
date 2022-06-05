a=int(input("Digite um número inteiro:"))

soma=0
p=10
b=0

while a!=0:
	b=a%p
	soma=soma+b
	a=a//p
	
print(soma)
