x1=float(input("Defina a coordenda x do ponto 1:"))
y1=float(input("Defina a coordenda y do ponto 1:"))
x2=float(input("Defina a coordenda x do ponto 2:"))
y2=float(input("Defina a coordenda y do ponto 2:"))

import math

r=(((x1-x2)**2)+((y1-y2)**2))
d=math.sqrt(r)

if(d>=10):
	print("longe")
else:
	print("perto")
