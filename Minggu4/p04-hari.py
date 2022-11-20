hari = int(input("Pilih hari: \n"))
match hari:
    case 1:
        print("Hari ini adalah Senin \n")
    case 2:
        print("Hari ini adalah Selasa \n")
    case 3:
        print("Hari ini adalah Rabu \n")
    case 4:
        print("Hari ini adalah Kamis \n")
    case 5:
        print("Hari ini adalah Jum'at \n")
    case 6:
        print("Hari ini adalah Sabtu \n")
    case 7:
        print("Hari ini adalah Minggu \n")
    case _:
        print("Hari ini tidak di kenal ")

#Inputkan data sebagai berikut:
#- Ketikan 1 untuk hari Senin       
# Ketikan 2 untuk hari Selasa
# Ketikan 3 untuk hari Rabu
# Ketikan 4 untuk hari Rabu
# Ketikan 5 untuk hari Kamis
# Ketikan 6 untuk hari Jum'at
# Ketikan 7 untuk hari Sabtu