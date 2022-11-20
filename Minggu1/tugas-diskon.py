namaBarang = input("Barang apa yang anda beli? ")
jumlahBarang = input("Berapa jumlah barang yang anda beli? ")
hargaBarang = input("Berapa harga barang tersebut? ")
diskon = input("Berapa besaran diskon barang tersebut? ")


jumlahBarang = int(jumlahBarang)
hargaBarang = int(hargaBarang)
diskon = int(diskon)


totalHarga = jumlahBarang * hargaBarang
diskon = totalHarga*(diskon/100)
totalSetelahDiskon = totalHarga - diskon


totalSetelahDiskon = str(totalSetelahDiskon)


print("harga dari "+namaBarang+" setelah diskon adalah Rp."+totalSetelahDiskon)
