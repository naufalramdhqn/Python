tugas = open("tugas.txt","r")
total = 0
a,b,c,d,e = 0,0,0,0,0

for nilai in tugas:
    nilai_mhs = int(nilai)
    total+=1

    if nilai_mhs>=90:
        a+=1

    elif nilai_mhs>=80 and nilai_mhs <90:
        b+=1

    elif nilai_mhs>=70 and nilai_mhs <80:
        c+=1

    elif nilai_mhs>=55 and nilai_mhs <70:
        d+=1

    else:
        e+=1

    print(f"persentase grade A adalah {a/total*100}%")