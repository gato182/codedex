#problema de pitagoras
#problema cuadratico
a = int(input("ingrese el numero: "))
b = int(input("ingrese el numero: "))
c = int(input("ingrese el numero: "))

c = (a**2 + b**2) ** 0.5

funcion = c

print(funcion)

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root1)
print(root2)
