students = ["jaka","rika","budi","ani","doni","eko","tika","fulan"]

print("Sorting elemen dari kecil ke besar: ")
for nama in sorted(students):
    print(f"{nama}\t", end='')

print("Sorting elemen dari besar ke kecil: ")
for nama in sorted(students, reverse=True):
    print(f"{nama}\t", end='')
    
print("\n Daftar otiginal: ")
for nama in students:
    print(f"{nama}\t", end='')