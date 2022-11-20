a = int(input("Input bilangan a : "))
b = int(input("Input bilangan b : "))

for i in range(1,a + 1):
    print("\n")
    for j in range (1,b + 1):
        kali = i*j
        print(f"Hasil perkalian dari {i} x {j} adalah {kali}")

        
else:
    print("\n\n""Tabel Perkalian Selesai")