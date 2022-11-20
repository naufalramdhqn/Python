from statistics import mean


with open("nilai_kuis.txt", "r") as nilai:
    nilai = nilai.read()

terbesar=0
terkecil=100

index2=0
list=[ ]

while index2 < len(nilai):
   str2 = f"{nilai[index2]}{nilai[index2+1]}"
   list.append(int(str2))

   index2 +=3

nilai_rata_rata = mean(list)
print("Rata-rata kelas ini adalah:",nilai_rata_rata)

index2=0
list=[]

while index2 < len(nilai):
   str2 = f"{nilai[index2]}{nilai[index2+1]}"
   list.append(str2)

   index2 +=3

for mark in list:
   mark =int(mark)
   if mark < terkecil:
      terkecil=mark
   if mark > terbesar:
      terbesar= mark

print(f"Nilai min adalah : {terkecil}")
print(f"Nilai max adalah : {terbesar}")