n = 0
x = 0

while n!= -1:
    n = int(input("Input sebuah bilangan: "))
    if n > x:
        x = n


print("Bilangan terbesar adalah",x)

if x%2 == 0 :
    print("Bilangan ini merupakan bilangan genap")
        
else:
    print("Bilangan ini merupakan bilangan ganjil")