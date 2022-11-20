kelasA = {"python","python","c++","java","go"}
kelasB = { "java","php","c++","java","python"}

print("HASIL UNION: ")
hasil= kelasA.union(kelasB)
for i in hasil:
    print(i, end ="\t")
    
print("\n----------------------------------")
print("HASIL INTERSECTION: ")
hasil = kelasA.intersection(kelasB)
for i in hasil:
    print(i, end ="\t")
    
print("\n----------------------------------")
print("HASIL DIFFERENCE: ")
hasil = kelasA.difference(kelasB)
for i in hasil:
    print(i, end ="\t")
    
print("\n----------------------------------")
print("HASIL SYMMETRIC DIFFERENFE: ")
hasil = kelasA.symmetric_difference(kelasB)
for i in hasil:
    print(i, end ="\t")
    