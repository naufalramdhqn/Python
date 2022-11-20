jumlah = int(input(("Berapa jumlah barang yang dibeli??\n")))
harga = int(input(("Berapa harga barang per itemm???\n")))

tanyaDiskon = input("Ada membernya kak?? (ya/tidak)\n")

if tanyaDiskon == "ya": 
    member = input("input jenis member ?? (silver/gold/platinum/diamond)\n")
    if member=="diamond":
        diskon =  90
    if member=="platinum":
        diskon: Literal[75] = 75
    elif member=="gold":
        diskon = 50
    elif member=="silver":
        diskon = 25
else:
    diskon = 0

total = (jumlah*harga) * (100-diskon)/100

if total <= 50000:
    member== "diamond"
    print("Selamat pesanan anda gratis")
else :
    print("total harga adalah Rp."+str(total))