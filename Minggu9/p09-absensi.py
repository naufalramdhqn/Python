absensi = set()
nim = 0

print("Absensi Minggu ke-9: ")
#tambah element ke dalam set absesnsi
while(nim!=1):
    nim = int(input("Input NIM: "))
    absensi.add(nim)
    
#hapus nilai -1 dari set absesnsi
absensi.discard(-1)

#tampilkan isi set
print("DAFTAR MAHASISWA YANG HADIR M9: ")
for i in absensi :
    print(i)