sisi = 0

while sisi<=0:
    sisi = int(input("Input sisi: "))

    if sisi<=0:
        print("Inputan salah! Sisi harus > 0")

luas= sisi * sisi 
print("Luas Adalah", luas)