harga = int(input("Input harga :"))
jumlah = int(input("Input Jumlah Barang: "))
member = input("Ada membernya kak???\n")

totalSebelumdiskon = (jumlah * harga)

match member:
    case "yes" | "YES" | "ya" | "YA" | "y":
        jenis = input("Input jenis member??? (silver/gold/platinum \n")
        
        match jenis:
            case "Silver" | "silver" | "sv" | "SV":
                diskon = 25
                total = (jumlah * harga) * (100-diskon)/100
                print("Total harga setelah diskon adalah Rp. ", total)
            case "Gold" | "gold" | "gd" | "GD":
                diskon = 50
                total = (jumlah * harga) * (100-diskon)/100
                print("Total harga setelah diskon adalah Rp. ", total)
            case "Platinum" | "platinum" | "pt" | "PT":
                diskon = 75
                total = (jumlah * harga) * (100-diskon)/100
                print("Total harga setelah diskon adalah Rp. ", total)
            case _:
                print("Member tidak dikenali")
    case _: 
        print("Total harga adalah Rp. ", totalSebelumdiskon)
    
