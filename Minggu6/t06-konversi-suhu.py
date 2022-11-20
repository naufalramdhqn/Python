c = float(input("Input suhu dalam celcius(c) : \n"))

konversi = (input("""Konversi kemana?? 
- Ketikkan F atau f untuk konversi ke Fahrenheit
- Ketikkan K atau k untuk konversi ke Kelvin
- Ketikkan R atau r untuk konversi ke Reamur
- Ketikkan A atau ALL untuk menampilkan semua konversi
"""))
print("=============================================")


match konversi:
    case "F" | "f":
        fahrenheit = (9/5) * c + 32
        print("Hasil konversi dari",c,"ke F adalah", fahrenheit)

    case "K" | "k":
        kelvin = c + 273
        print("Hasil konversi dari",c,"ke K adalah", kelvin)

    case "R" | "r":
        reamur = (4/5) * c
        print("Hasil konversi dari",c,"ke R adalah", reamur)

    case "A" | "ALL":
        fahrenheit = (9/5) * c + 32
        kelvin = c + 273
        reamur = (4/5) * c

        c = float(kelvin)
        print("Hasil konversi dari",c,"ke F adalah", fahrenheit)
        print("Hasil konversi dari",c,"ke K adalah", kelvin)
        print("Hasil konversi dari",c,"ke R adalah", reamur)