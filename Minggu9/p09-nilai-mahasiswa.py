surveys = {
    "Fulan": 650,
    "Kirana": 900,
    "Doni": 500,
    "Lisa": 450,
    "Joko": 900,
    "Gilang": 850
}

#konversi dictionary ke list0
nilai = list(surveys.values())

#tampilkan koleksi data setelah di konversi
print(nilai)

#sorting list dari kecil ke besar secara permanen
#nilai.sort

#sorting list dari besar ke kecil secara permanen
nilai.sort(reverse = True)

print(nilai)

print(f"""
Hasil dari survey menunjukkan nilai
terendah yaitu {nilai[-1]} diberikan sebanyak
{nilai.count(nilai[-1])} kali oleh {len(surveys)} responden.
""")