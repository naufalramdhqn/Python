tahun = int(input("Input tahun: "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print(tahun,"ADALAH Tahun kabisa")
        else:
            print(tahun,"Bukan Tahun Kabisat")
    else:
        print(tahun, "ADALAH Tahun Kabisat")
else:
    print(tahun, "BUKAN Tahun Kabisat")