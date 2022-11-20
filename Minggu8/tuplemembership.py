cupons = ("murah101", "hemat1408", "gajian01", "merdeka17", "userBaru")

q = input("Input kupon yang anda miliki: ")

if q not in cupons:
    print("Kupon anda tidak valid!")
else:
    print(f"Selamat anda mendapat diskon dengan kode {q}")