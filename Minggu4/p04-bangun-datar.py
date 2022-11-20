program = input("Tentukan Program: \n")

match program:
    case "PSG" | "persegi":
        hitung = input("Pilih jenis perhitungan! LUAS/L dan KELILING/K: \n")
        s = float(input("Inputkan sisi: \n"))

        match hitung:
            case "L" | "LUAS":
                luas = s**2
                print("Luas persegi adalah ",luas)

            case "K" | "KELILING":
                    keliling = 4*s
                    print("Keliling adalah ", keliling)

            case _:
                print("Jenis perhitungan tidak dikenal")
    case "LKR" | "Lingkaran":
        hitung = input("Pilih jenis perhitungan! LUAS/L dan KELILING/K: \n")
        r = float(input("Inputkan jari-jari: \n"))

        match hitung:
            case "L" | "LUAS":
                luas = 3.14*r
                print("Luas lingkaran adalah ", luas)
            case "K" | "KELILING":
                keliling = 2*3.14*r
                print("keliling lingkaran adalah ", keliling)
            case _:
                print("jenis perhitungan tidak dikenal")

    case _:
        print("Program tidak dikenal")

