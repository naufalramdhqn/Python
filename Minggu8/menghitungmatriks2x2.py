x = [
    [12,17],
    [14,25]
]

y = [
    [5,8],
    [6,7]
]

jumlah = [
    [0,0],
    [0,0]
]

for i in range(len(x)):
    for j in range(len(y[0])):
        jumlah[i][j] = x[i][j] + y[i][j]

print("Hasil penjumlahan matriks x dan y adalah:")
for i in jumlah:
    print(i)
