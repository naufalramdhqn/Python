import random

indexes = set()
indexesClone = set()

for i in range(1, 5):
    nilai = random.randint(1, 10)
    indexes.add(nilai)
    indexesClone.add(nilai)

looped = len(indexes)
life = 3
startGuest = 1
EndGuest = 10

print(f"Total yang harus anda tebak adalah {looped} angka! Selamat mencoba")
print(indexes)

for i in range(5):
    guestNilai = int(
        input(f"Tebak sebuah angka dari {startGuest} - {EndGuest} : "))

    if guestNilai in indexes:
        indexes.remove(guestNilai)
        life = life + 1

    if len(indexes) == 0:
        print("Selamat anda menang dengan sempurna tanpa kehilangan nyawa")
        break

    if guestNilai not in indexes:
        life = life - 1    

    if life == 0:
        print(
            f"Anda gagal karena tidak dapat menjawab nilai berikut : {indexesClone}")
        break

if life == 1:
    print("Selamat anda menang dengan sisa 1 nyawa")
if life == 2:
    print("Selamat anda menang dengan sisa 2 nyawa")
if life == 3:
    print("Selamat anda menang dengan sempurna tanpa kehilangan nyawa")
