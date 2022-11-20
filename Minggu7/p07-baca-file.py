grade = open("Minggu7/grade.txt","r")

nilai =  grade.read()

if int(nilai)>70:
    print("ANDA LULUS")
else:
    print("ANDA GAGAL")

print(nilai)

grade.close()