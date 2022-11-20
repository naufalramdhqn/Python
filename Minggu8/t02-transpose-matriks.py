m = [
    [12,7],
    [4,5],
    [3,8]
]

for i in m:
    print(i)

transpos = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        
print("Hasil setelah transpos adalah:")
for i in transpos:
    print(i)