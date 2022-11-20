detik = int(input("Input jumalh detik: "))

jam     = detik // 3600;
sisa    = detik % 3600;
menit   = sisa // 60;
Detik   = sisa % 60;

print("Konversi",detik,"detik adalah",jam,"Jam,",menit,"Menit,",Detik,"Detik")