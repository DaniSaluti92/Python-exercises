s=int(input("Por favor, entre com o número de segundos que deseja converter:"))
a=s//86400
d=s%86400
b=d//3600
h=d%3600
c=h//60
d=h%60
print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos")
