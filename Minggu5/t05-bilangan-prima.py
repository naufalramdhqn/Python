bilprima = 0

while  bilprima%2 == 0 or bilprima <=1:
    bilprima = int(input("Input sebuah bilangan: "))
    if bilprima <=1:
        print("inputan salah. Ulangi lagi.")
    elif bilprima%2 == 0 and not bilprima ==2:
        print(bilprima,"BUKAN bilangan prima")
        break
    elif bilprima == 2:
        print(bilprima,"adalah bilangan prima.")
        break
    else:
        print(bilprima,"adalah bilangan prima.")