bilangan = open("bilangan.txt", "r")
total = 0
genap = 0
ganjil = 0

for i in bilangan :
    total = total+1
    if int(i) % 2 == 0:
        bil = open("genap.txt", "a")
        bil.write(i)
        genap = genap+1
    else:
        bill = open("ganjil.txt", "a")
        bill.write(i)
        ganjil = ganjil+1


print("Total genap di file adalah "+str(int(genap/total*100)) + "%")
print("Total ganjil di file adalah "+str(int(ganjil/total*100)) + "%")