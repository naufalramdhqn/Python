tugas = int(input(("Input nilai tugas: ")))

uts = int(input(("Input nilai UTS: ")))

uas = int(input(("Input nilai UAS: ")))

nilaiakhir = (tugas*0.2)+(uts*0.4)+(uas*0.4) 

print("nilai akhir mahasiswa adalah :"+str(nilaiakhir))

if (86 <= nilaiakhir <= 100):
    print ("Grade A")
elif(75 <= nilaiakhir <= 84):
    print ("Grade B")
elif (60 <= nilaiakhir <= 74):
    print ("Grade C")
elif (46 <= nilaiakhir <= 59):
    print ("Grade D")
elif (nilaiakhir <= 46):
    print ("Grade E")
else:
    print ("anda gagal")
