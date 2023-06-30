a = int(input("What do you have left in peso?: "))
b = int(input("What do you have left in reais?: "))
c = int(input("What do you have left in soles?: "))

h = a * 0.00087
j = b * 0.75
total = h + j + c
print(total)

us = total / 3.65

print(us)
